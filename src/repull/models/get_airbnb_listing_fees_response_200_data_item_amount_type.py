from enum import Enum

class GetAirbnbListingFeesResponse200DataItemAmountType(str, Enum):
    FLAT = "flat"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
