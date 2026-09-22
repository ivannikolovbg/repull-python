from enum import Enum

class ReservationRequestCreatedEventEvent(str, Enum):
    RESERVATION_REQUEST_CREATED = "reservation.request.created"

    def __str__(self) -> str:
        return str(self.value)
