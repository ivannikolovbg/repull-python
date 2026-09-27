from enum import Enum

class CancelReservationResponse200Status(str, Enum):
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)
