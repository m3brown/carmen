import aiohttp


async def __fetch(session, url):
    """
    This function is the equivalent of requests.get() but with aiohttp.
    aiohttp is like the popular libraries 'requests' and 'urllib2', but it
    is async-compatible.
    """
    async with session.get(url) as response:
        return await response.json()


async def get_latest_country():
    # Getting the country from a REST API in an async-friendly way requires an
    # asyncio connection pool. aiohttp.ClientSession() sets that up for us.
    async with aiohttp.ClientSession() as session:
        return await __fetch(session, "http://localhost:5000")
