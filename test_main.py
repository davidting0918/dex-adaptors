from unittest import IsolatedAsyncioTestCase

from dex_adaptors.uniswap_v3 import UniswapV3


class TestUniswapV3(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.exchange = UniswapV3()

    async def asyncTearDown(self):
        pass

    async def test_get_pool_data(self):
        ezETH_WETH_pool_address = "0xbe80225f09645f172b079394312220637c440a63"
        data = await self.exchange.get_pool_data(ezETH_WETH_pool_address)
        self.assertTrue(data)

        return data

    async def test_get_pool_candlesticks(self):
        ezETH_WETH_pool_address = "0xbe80225f09645f172b079394312220637c440a63"
        num = 1000
        data = await self.exchange.get_pool_token_candlesticks(ezETH_WETH_pool_address, num)
        self.assertTrue(data)

        return data

    async def test_get_pool_price_canlesticks(self):
        ezETH_WETH_pool_address = "0xbe80225f09645f172b079394312220637c440a63"
        num = 1000
        data = await self.exchange.get_pool_price_candlesticks(ezETH_WETH_pool_address, num)
        self.assertTrue(data)

        return data
