from enum import Enum

class AirbnbReservationStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    DENIED = "denied"
    INQUIRY = "inquiry"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
