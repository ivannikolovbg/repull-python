from enum import Enum

class AirbnbPricingWriteRequestFeesType0ItemAmountType(str, Enum):
    FLAT = "flat"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
