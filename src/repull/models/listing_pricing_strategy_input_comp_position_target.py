from enum import Enum

class ListingPricingStrategyInputCompPositionTarget(str, Enum):
    ABOVE = "above"
    BELOW = "below"
    MATCH = "match"

    def __str__(self) -> str:
        return str(self.value)
