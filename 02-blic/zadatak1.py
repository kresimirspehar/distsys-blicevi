import aiohttp
import asyncio
import time
import aiosqlite


from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/getJokes")
async def get_Jokes_db(req):
    try:
        jokes = []
        client = []
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:      
          
            for a in range(6):
                for b in range(2):
                    jokes.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
                    client.append(asyncio.create_task(session.get("https://randomuser.me/api/")))

            res1 = await asyncio.gather(*jokes)
            res2 = await asyncio.gather(*client)

            json_data_jokes = [await x.json() for x in res1]
            json_data_client = [await x.json() for x in res2]

            jokes = asyncio.create_task(sendToParserJokes(json_data_jokes, session))
            client = asyncio.create_task(sendToParserClient(json_data_client, session))
            service2_response = await jokes
            service3_response = await client

        return web.json_response({"status:":"ok"}, status=200)
    except Exception as e:
        return web.json_response({"status:":"fail","message:": str(e)})


async def sendToParserJokes(json_activities, session):
    for x in range(len(json_activities)):
        async with session.post("http://localhost:8085/filterJoke", json=json_activities[x]) as resp:
            service2_response = await resp.text()
    return service2_response

async def sendToParserClient(json_activities, session):
    for x in range(len(json_activities)):
        async with session.post("http://localhost:8085/filterUser", json=json_activities[x]) as resp:
            service2_response = await resp.text()
    return service2_response



app = web.Application()

app.router.add_routes(routes)

web.run_app(app)