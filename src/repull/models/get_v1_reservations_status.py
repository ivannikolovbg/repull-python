from enum import Enum

class GetV1ReservationsStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
