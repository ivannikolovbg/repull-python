from enum import Enum

class MarketMyListingType(str, Enum):
    MINE = "mine"

    def __str__(self) -> str:
        return str(self.value)
