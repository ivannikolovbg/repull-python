from enum import Enum

class ReservationRequestUpdatedEventEvent(str, Enum):
    RESERVATION_REQUEST_UPDATED = "reservation.request.updated"

    def __str__(self) -> str:
        return str(self.value)
