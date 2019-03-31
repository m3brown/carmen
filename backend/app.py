import responder
import asyncio
from country_api_wrapper import get_latest_country

api = responder.API()


@api.route("/")
async def home(req, resp):
    """
    A standard REST endpoint for getting country info.
    """
    resp.media = await get_latest_country()
    resp.media["info"] = "This is a proxied response"


@api.route("/ws", websocket=True)
async def websocket(ws):
    """
    A websocket endpoint for subscribing to country info.
    """
    await ws.accept()
    # TODO: add ws session to background task
    while True:
        country = await get_latest_country()
        await ws.send_json(country)
        await asyncio.sleep(5)
    await ws.close()


if __name__ == "__main__":
    api.run()
