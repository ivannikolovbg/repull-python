from enum import Enum

class BookingReservationStatus(str, Enum):
    CANCELLED = "cancelled"
    MODIFIED = "modified"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
