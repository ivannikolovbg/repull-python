from enum import Enum

class TiketAvailabilityUpdateRequestType(str, Enum):
    AVAILABILITY = "availability"
    RATES = "rates"
    RESTRICTIONS = "restrictions"

    def __str__(self) -> str:
        return str(self.value)
