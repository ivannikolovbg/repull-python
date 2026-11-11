from enum import Enum

class ReservationMessageReadEventEvent(str, Enum):
    RESERVATION_MESSAGE_READ = "reservation.message.read"

    def __str__(self) -> str:
        return str(self.value)
