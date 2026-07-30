from enum import Enum

class AirbnbAvailabilityWriteRequestType(str, Enum):
    CALENDAR = "calendar"
    RULES = "rules"

    def __str__(self) -> str:
        return str(self.value)
