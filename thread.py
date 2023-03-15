import threading
import time
import asyncio
import logging
import dns
import dns.resolver
from models.domains import domains
from config import database
from models.dns import dnsTable
from models.logs import logs
from datetime import datetime



logging.basicConfig(filename='register_dns.log', encoding='utf-8', level=logging.DEBUG)

async def call_dns():
    now = datetime.now()
    logging.info(now.strftime("%m/%d/%Y, %H:%M:%S") + " Start process to study dns")
    await database.connect()
    #consult actual domains active
    query = domains.select().where(domains.columns.deleted_at == None)
    #consult actuals dns and deactivate all registers
    results = await database.fetch_all(query)
    for result in results:
        logging.info("Study domain : "+result.domain)

        queryToDeactivateAllDNSByDomain = dnsTable.update().values(state = 1).where(dnsTable.columns.id_domain == result.id)
        await database.execute(queryToDeactivateAllDNSByDomain)
        queryActualdns = dnsTable.select().where(dnsTable.columns.id_domain == result.id)
        resultsActualdns = await database.fetch_all(queryActualdns)
        #consult dns
        ptNS = dns.resolver.resolve(result.domain, 'NS')
        for pt in ptNS:
            #find the dns of the existing ones
             found = [p for p in resultsActualdns if p.dns == str(pt)]
             executeQueryToDNS = ""
             #validate if not exist create the new register and save log and audit
             if(len(found) == 0):
                 logMssg = "The domain "+result.domain+" has a new DNS "+ str(pt)
                 logging.warning(logMssg)
                 insertaudit = logs.insert().values(id_domain = result.id, log = logMssg)
                 executeQueryToDNS = dnsTable.insert().values(dns = str(pt), id_domain = result.id)
                 await database.execute(insertaudit)    
            #if exist change the state to active
             else:
                 executeQueryToDNS = dnsTable.update().values(state = 0).where(dnsTable.columns.dns == str(pt))
             await database.execute(executeQueryToDNS)    
        
    await database.disconnect()
    logging.info(now.strftime("%m/%d/%Y, %H:%M:%S") + " End process to study dns")

    

def timer(timer_runs):

    while timer_runs.is_set():
        asyncio.run(call_dns())
        #time to repeat the thread
        time.sleep(60)

        

#use threading and asyncio for obtain dns to domains, validate the information and capture logs to database
timer_runs = threading.Event()

timer_runs.set()

t = threading.Thread(target=timer, args=(timer_runs,))

t.start()



