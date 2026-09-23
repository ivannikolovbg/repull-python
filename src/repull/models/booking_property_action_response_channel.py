from enum import Enum

class BookingPropertyActionResponseChannel(str, Enum):
    BOOKING = "booking"

    def __str__(self) -> str:
        return str(self.value)
