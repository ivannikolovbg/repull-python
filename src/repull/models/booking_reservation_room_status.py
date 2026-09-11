from enum import Enum

class BookingReservationRoomStatus(str, Enum):
    CANCELLED = "cancelled"
    MODIFIED = "modified"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
