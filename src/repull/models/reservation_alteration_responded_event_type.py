from enum import Enum

class ReservationAlterationRespondedEventType(str, Enum):
    RESERVATION_ALTERATION_RESPONDED = "reservation.alteration.responded"

    def __str__(self) -> str:
        return str(self.value)
