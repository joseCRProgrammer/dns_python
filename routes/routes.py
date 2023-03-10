from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from controllers.dnsController import list_dns
from controllers.dnsController import create_dns




#build routes to get and save dns basic information
routes = [
    Route("/", endpoint=list_dns,  methods=["GET"]),
    Route("/dns", endpoint=create_dns,  methods=["POST"]),
]