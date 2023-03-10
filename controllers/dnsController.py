from models.dns import dns
from config import database
from starlette.responses import JSONResponse


#build controller function to logic and principal parameters to crud
async def list_dns(request):
    query = dns.select()

    results = await database.fetch_all(query)
    content = [
        {
            "id": result["id"],
            "dns": result["name"],
            "description": result["description"],
            
        }
        for result in results
    ]
    return JSONResponse(content)


async def create_dns(request):
    
    data = await request.json()
    
    query = dns.insert().values(
       dns=data["dns"],
       description=data["description"]
    )
    results = await database.execute(query)
    
    print(results)
    
    return JSONResponse({
        "message": "success",
        "status": "true"
    })


