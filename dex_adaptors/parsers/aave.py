from .base import Parser

class AaveV2Parser(Parser):
    def __init__(self):
        super().__init__()

    def parse_tvl_data(self, data: dict) -> dict:

        return data