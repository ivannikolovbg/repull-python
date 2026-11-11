from enum import Enum

class ReservationMessageReactionEventEvent(str, Enum):
    RESERVATION_MESSAGE_REACTION = "reservation.message.reaction"

    def __str__(self) -> str:
        return str(self.value)
