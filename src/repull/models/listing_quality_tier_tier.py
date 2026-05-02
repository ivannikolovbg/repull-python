from enum import Enum

class ListingQualityTierTier(str, Enum):
    BUDGET = "budget"
    LUXURY = "luxury"
    STANDARD = "standard"
    UPSCALE = "upscale"

    def __str__(self) -> str:
        return str(self.value)
