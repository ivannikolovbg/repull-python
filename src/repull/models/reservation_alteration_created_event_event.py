from enum import Enum

class ReservationAlterationCreatedEventEvent(str, Enum):
    RESERVATION_ALTERATION_CREATED = "reservation.alteration.created"

    def __str__(self) -> str:
        return str(self.value)
