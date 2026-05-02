from enum import Enum

class ListingPricingStrategyInputMode(str, Enum):
    AUTO = "auto"
    RECOMMEND = "recommend"

    def __str__(self) -> str:
        return str(self.value)
