from enum import Enum

class ListTiketReservationsStatus(str, Enum):
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
