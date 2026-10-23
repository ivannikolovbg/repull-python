from enum import Enum

class ListingFeeAmountType(str, Enum):
    FLAT = "flat"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
