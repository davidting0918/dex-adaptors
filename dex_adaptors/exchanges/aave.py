from .https_base import PublicClient

class AaveV2Unified(PublicClient):
    base_endpoint = "https://aave-api-v2.aave.com"

    def __init__(self):
        super().__init__()
        self.name = 'aave_v2'

    async def get_tvl_data(self) -> dict:
        return await self._get(f"{self.base_endpoint}/data/tvl")

    async def get_markets_data(self) -> dict:
        return await self._get(f"{self.base_endpoint}/data/markets-data")

    async def get_daily_volume_24hrs(self) -> dict:
        return await self._get(f"{self.base_endpoint}/data/daily-volume-24-hours")

    async def get_pools_data(self) -> dict:
        return await self._get(f"{self.base_endpoint}/data/pools")

    async def get_rates_history(self, reserveId: str, _from: int = None, resoilutionInHours: int = None) -> dict:
        params = {
            k: v for k, v in {
                "reserveId": reserveId,
                "from": _from,
                "resolutionInHours": resoilutionInHours
            }.items()
            if v is not None
        }
        return await self._get(f"{self.base_endpoint}/data/rates-history", params=params)

    async def get_v1_liquidity(self, poolId: str, date: str = None) -> dict:
        params = {
            k: v for k, v in {
                "poolId": poolId,
                "date": date
            }.items()
            if v is not None
        }
        return await self._get(f"{self.base_endpoint}/data/liquidity/v1", params=params)

    async def get_v2_liquidity(self, poolId: str, date: str = None) -> dict:
        params = {
            k: v for k, v in {
                "poolId": poolId,
                "date": date
            }.items()
            if v is not None
        }
        return await self._get(f"{self.base_endpoint}/data/liquidity/v2", params=params)