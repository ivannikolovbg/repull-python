from enum import Enum

class ReservationCreatedEventType(str, Enum):
    RESERVATION_CREATED = "reservation.created"

    def __str__(self) -> str:
        return str(self.value)
