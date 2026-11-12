from enum import Enum

class AccountUnitsAddedPayloadProvider(str, Enum):
    BOOKING_EXTRANET = "booking_extranet"

    def __str__(self) -> str:
        return str(self.value)
