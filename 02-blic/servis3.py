import aiohttp
import asyncio
import time
import aiosqlite

from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterJoke")
async def get_filter_joke(request):
    try:
        req = await request.json()

        var2 = []
        var2.append({"setup": req.get("setup")})
        var2.append({"punchline": req.get("punchline")})

        return web.json_response({"Status": "ok","joke":request}, status=200)

    except Exception as e:
        return web.json_response({"Status": "error"}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)