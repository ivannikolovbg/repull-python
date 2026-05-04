from enum import Enum

class ReservationUpdatedEventType(str, Enum):
    RESERVATION_UPDATED = "reservation.updated"

    def __str__(self) -> str:
        return str(self.value)
