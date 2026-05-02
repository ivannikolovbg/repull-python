from enum import Enum

class ListingPricingRecommendationStatus(str, Enum):
    APPLIED = "applied"
    DECLINED = "declined"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
