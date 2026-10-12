from enum import Enum

class GetHotelResponse200Source(str, Enum):
    BOOKING = "booking"
    PMS = "pms"

    def __str__(self) -> str:
        return str(self.value)
