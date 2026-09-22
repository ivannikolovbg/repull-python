from enum import Enum

class BookingRoomsRatesResponseSource(str, Enum):
    BOOKING = "booking"
    MIRROR = "mirror"

    def __str__(self) -> str:
        return str(self.value)
