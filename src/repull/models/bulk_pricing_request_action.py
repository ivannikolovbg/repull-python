from enum import Enum

class BulkPricingRequestAction(str, Enum):
    APPLY = "apply"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
