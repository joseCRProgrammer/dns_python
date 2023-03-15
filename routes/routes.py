from starlette.routing import Route
from controllers.dnsController import list_domain
from controllers.dnsController import create_dns
from starlette.responses import JSONResponse



routes = [
    Route("/", endpoint=list_domain,  methods=["GET"]),
    Route("/dns", endpoint=create_dns,  methods=["POST"]),
]