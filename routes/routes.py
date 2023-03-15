from starlette.routing import Route
from controllers.dnsController import *

routes = [
    Route("/", endpoint=list_domain, methods=["GET"]),
    Route("/domains", endpoint=create_domain, methods=["POST"]),
    Route("/delete/domain/{id:int}", endpoint=delete_domain, methods=["POST"]),

    
]