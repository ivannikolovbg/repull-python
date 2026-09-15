from enum import Enum

class AirbnbCalendarOperationBusySubtype(str, Enum):
    BLOCKED_BY_HOST = "BLOCKED_BY_HOST"
    OUTSIDE_RESERVATION = "OUTSIDE_RESERVATION"

    def __str__(self) -> str:
        return str(self.value)
