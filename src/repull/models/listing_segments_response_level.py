from enum import Enum

class ListingSegmentsResponseLevel(str, Enum):
    COMP_SET = "comp_set"
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
