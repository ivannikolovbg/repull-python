from enum import Enum

class ListingHotelType0Source(str, Enum):
    BOOKING = "booking"
    PMS = "pms"

    def __str__(self) -> str:
        return str(self.value)
