from enum import Enum

class GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1(str, Enum):
    BLOCK = "block"
    ICAL = "ical"
    RESERVATION = "reservation"

    def __str__(self) -> str:
        return str(self.value)
