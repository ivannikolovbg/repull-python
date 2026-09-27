from enum import Enum

class ReservationMessageUpdatedEventEvent(str, Enum):
    RESERVATION_MESSAGE_UPDATED = "reservation.message.updated"

    def __str__(self) -> str:
        return str(self.value)
