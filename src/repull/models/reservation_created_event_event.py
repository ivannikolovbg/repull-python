from enum import Enum

class ReservationCreatedEventEvent(str, Enum):
    RESERVATION_CREATED = "reservation.created"

    def __str__(self) -> str:
        return str(self.value)
