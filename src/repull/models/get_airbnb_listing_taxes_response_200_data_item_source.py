from enum import Enum

class GetAirbnbListingTaxesResponse200DataItemSource(str, Enum):
    AIRBNB_COLLECTED = "airbnb_collected"
    PASS_THROUGH = "pass_through"

    def __str__(self) -> str:
        return str(self.value)
