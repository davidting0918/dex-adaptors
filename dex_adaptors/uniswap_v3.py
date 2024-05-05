from .exchange.uniswap_v3 import UniswapV3Unified
from .parsers.uniswap_v3 import UniswapV3Parser


class UniswapV3(UniswapV3Unified, UniswapV3Parser):
    base_endpoint = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"

    def __init__(self):
        super().__init__(base_endpoint=self.base_endpoint)

    async def get_pool_data(self, pool_address: str) -> dict:
        return self.parse_pool_data(await self._get_pool_data(address=pool_address))

    async def get_pool_token_candlesticks(self, pool_address: str, num: int) -> list:
        limit = 1000
        results = self.parse_pool_token_candlesticks(
            await self._get_pool_token_candlesticks(pool_address=pool_address, num=limit)
        )
        return results

    async def get_pool_price_candlesticks(self, pool_address: str, num: int) -> list:
        limit = 1000
        results = self.parse_pool_price_candlesticks(
            await self._get_pool_price_candlesticks(pool_address=pool_address, num=limit)
        )
        return results
