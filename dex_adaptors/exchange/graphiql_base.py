from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


class GqlClient:
    def __init__(self, base_endpoint: str):
        self.base_endpoint = base_endpoint
        self.transport = AIOHTTPTransport(url=self.base_endpoint)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    async def request(self, query: str) -> dict:
        query = gql(query)
        return await self.handle_response(await self.client.execute_async(query))

    async def handle_response(self, response: dict) -> dict:
        return response
