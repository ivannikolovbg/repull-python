from enum import Enum

class ListingPricingStrategyMode(str, Enum):
    AUTO = "auto"
    RECOMMEND = "recommend"

    def __str__(self) -> str:
        return str(self.value)
