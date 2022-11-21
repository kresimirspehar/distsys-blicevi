import aiohttp
import asyncio
import time
import aiosqlite

from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterUser")
async def get_podaci(request):

    request = await request.json()
    var1 = request
    var1 = var1.get("finish")
   
    var1 = var1[0].get("name")
    zad = []
    zad.append({"ime": var1.get("ime"),"prezime":var1.get("last")})
    var1 = request.get("finish")

    zad.append({"city": var1[0].get("city"),"email":var1[0].get("email")})
    var1 = []

    return web.json_response({"Status": "ok","message":request}, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)