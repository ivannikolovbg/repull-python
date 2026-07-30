from enum import Enum

class AirbnbCalendarOperationAvailability(str, Enum):
    AVAILABLE = "available"
    DEFAULT = "default"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
