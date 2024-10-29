from .exchanges.aave import AaveV2Unified
from .parsers.aave import AaveV2Parser


class AaveV2(object):

    def __init__(self):
        self.client = AaveV2Unified()
        self.parser = AaveV2Parser()

    async def get_tvl_data(self):
        return self.parser.parse_tvl_data(await self.client.get_tvl_data())



    async def close(self):
        await self.client.close()