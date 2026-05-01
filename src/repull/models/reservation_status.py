from enum import Enum

class ReservationStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
