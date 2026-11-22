from enum import Enum

class GetAirbnbListingFeesResponse200DataItemChargeType(str, Enum):
    PER_GROUP = "PER_GROUP"
    PER_PERSON = "PER_PERSON"
    PER_PET = "PER_PET"

    def __str__(self) -> str:
        return str(self.value)
