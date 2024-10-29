import aiohttp
import json


class PublicClient(object):
    name = None

    def __init__(self) -> None:
        self._session = aiohttp.ClientSession()

    async def _request(self, method: str, url: str, **kwargs):

        if method == "GET":
            async with self._session.get(url, **kwargs) as response:
                return await self._handle_response(response)
        elif method == "POST":
            async with self._session.post(url, **kwargs) as response:
                return await self._handle_response(response)
        else:
            raise ValueError(f"Invalid method: {method}")

    async def _handle_response(self, response: aiohttp.ClientResponse):
        if response.status == 200:
            try:
                return await response.json()
            except Exception as e:
                print(e)
                return json.loads(await response.text())
        else:
            raise Exception(f"Error {response.status} {response.reason} {await response.text()}")

    async def _get(self, url: str, **kwargs):
        return await self._request("GET", url, **kwargs)

    async def _post(self, url: str, **kwargs):
        return await self._request("POST", url, **kwargs)

    async def close(self):
        await self._session.close()