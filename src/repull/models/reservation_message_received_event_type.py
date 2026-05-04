from enum import Enum

class ReservationMessageReceivedEventType(str, Enum):
    RESERVATION_MESSAGE_RECEIVED = "reservation.message.received"

    def __str__(self) -> str:
        return str(self.value)
