from enum import Enum

class BookingAvailabilityUpdateStatus(str, Enum):
    AVAILABLE = "available"
    ON_REQUEST = "on_request"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
