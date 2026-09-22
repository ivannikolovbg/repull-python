from enum import Enum

class BookingRateWriteOccupancySource(str, Enum):
    RATE_PLAN = "rate_plan"
    REQUEST = "request"
    ROOM = "room"

    def __str__(self) -> str:
        return str(self.value)
