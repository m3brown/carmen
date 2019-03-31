import responder
import aiohttp
import asyncio

api = responder.API()

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def get_latest_country():
    async with aiohttp.ClientSession() as session:
        return await fetch(session, 'http://localhost:5000')

@api.route('/ws', websocket=True)
async def websocket(ws):
    await ws.accept()
    # TODO: add ws session to background task
    while True:
        country = await get_latest_country() 
        await ws.send_text(country['abbreviation'])
        await asyncio.sleep(5)
    await ws.close()

api.run()
