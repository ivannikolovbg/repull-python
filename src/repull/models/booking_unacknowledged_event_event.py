from enum import Enum

class BookingUnacknowledgedEventEvent(str, Enum):
    BOOKING_UNACKNOWLEDGED = "booking.unacknowledged"

    def __str__(self) -> str:
        return str(self.value)
