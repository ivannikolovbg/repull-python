from enum import Enum

class BookingAvailabilityUpdateRequestType(str, Enum):
    AVAILABILITY = "availability"
    DERIVED_PRICING = "derived-pricing"
    RATES = "rates"

    def __str__(self) -> str:
        return str(self.value)
