from enum import Enum

class ReservationCancelledEventType(str, Enum):
    RESERVATION_CANCELLED = "reservation.cancelled"

    def __str__(self) -> str:
        return str(self.value)
