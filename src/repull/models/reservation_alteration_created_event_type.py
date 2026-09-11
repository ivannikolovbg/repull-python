from enum import Enum

class ReservationAlterationCreatedEventType(str, Enum):
    RESERVATION_ALTERATION_CREATED = "reservation.alteration.created"

    def __str__(self) -> str:
        return str(self.value)
