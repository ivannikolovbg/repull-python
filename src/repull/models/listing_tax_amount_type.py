from enum import Enum

class ListingTaxAmountType(str, Enum):
    FLAT = "flat"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
