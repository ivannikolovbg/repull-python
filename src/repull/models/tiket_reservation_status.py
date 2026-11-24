from enum import Enum

class TiketReservationStatus(str, Enum):
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
