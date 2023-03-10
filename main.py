from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from routes.routes import routes
from config import database
from threads.thread import t

#use startlette to async function
app = Starlette(debug=True, 
               routes=routes,
               on_startup=[database.connect],
               on_shutdown=[database.disconnect])


#execute thread to read dns
t.start()