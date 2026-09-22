from enum import Enum

class ReservationAlterationRespondedEventEvent(str, Enum):
    RESERVATION_ALTERATION_RESPONDED = "reservation.alteration.responded"

    def __str__(self) -> str:
        return str(self.value)
