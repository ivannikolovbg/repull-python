from enum import Enum

class ReservationMessageSentEventEvent(str, Enum):
    RESERVATION_MESSAGE_SENT = "reservation.message.sent"

    def __str__(self) -> str:
        return str(self.value)
