from enum import Enum

class UpdateAirbnbListingFeesBodyFeesItemAmountType(str, Enum):
    FLAT = "flat"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
