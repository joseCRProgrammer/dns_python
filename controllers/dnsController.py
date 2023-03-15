from models.domains import domains
from config import database
from starlette.responses import JSONResponse
from sqlalchemy.sql import func
from models.dns import dnsTable
from models.logs import logs
from starlette.responses import JSONResponse
import datetime


#build controller function to logic and principal parameters to crud
#call domain that deleted_at is null

async def list_domain(request):
    query = domains.select().where(domains.columns.deleted_at == None)

    results = await database.fetch_all(query)
    
    response = []
    for result in results:
        audit = []
        dns = []
        queryFindAllDnsByIdDomain = dnsTable.select().where(dnsTable.columns.id_domain == result.id)
        queryFindAllLogsByIdDomain = logs.select().where(logs.columns.id_domain == result.id)
        dns = await database.fetch_all(queryFindAllDnsByIdDomain)
        audit = await database.fetch_all(queryFindAllLogsByIdDomain)
        data = {
            "id": result.id,
            "domain": result.domain,
            "description": result.domain,
            "dns":[{
                "id":value.id,
                "dns":value.dns,
                "state":"ACTIVE" if value.state == 0 else "DEACTIVE",
                "created_at": value.created_at.isoformat(),
                "updated_at": value.updated_at.isoformat()
             } for value in dns],
            "audit":[{
                "id":value.id,
                "log":value.log,
             } for value in audit],
            "created_at": result.created_at.isoformat(),
            "updated_at": result.updated_at.isoformat()   
        }      
        response.append(data)
        
    
    #return response
    return JSONResponse(response)
    


#method to create_domain
async def create_domain(request):
    
    data = await request.json()
    
    queryToValidate = domains.select().where(domains.columns.domain == data['domain'])
    count = await database.fetch_all(queryToValidate)
    if(len(count) > 0):
        
        return JSONResponse({
        "message": "The domain exist",
        "status": "false"
        })
        
    query = domains.insert().values(
       domain=data["domain"],
       description=data["description"]
    )
    
    await database.execute(query)
        
    return JSONResponse({
        "message": "success",
        "status": "true"
    })
    
#method to delete domain
async def delete_domain(request):
    id = request.path_params['id']
    query = domains.update().values(deleted_at = datetime.datetime.utcnow()).where(domains.columns.id == id)
    await database.execute(query)
        
    return JSONResponse({
        "message": "success",
        "status": "true"
    })
    
    


