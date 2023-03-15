from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from routes.routes import routes
from config import database


app = Starlette(debug=True, 
               routes=routes,
               on_startup=[database.connect],
               on_shutdown=[database.disconnect])

