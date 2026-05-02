from enum import Enum

class ListingPricingApplyRequestAction(str, Enum):
    APPLY = "apply"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
