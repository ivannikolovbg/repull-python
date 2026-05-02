from enum import Enum

class ListingPricingHistoryEntryStatus(str, Enum):
    APPLIED = "applied"
    DECLINED = "declined"
    OVERRIDDEN = "overridden"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
