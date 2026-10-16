from enum import Enum

class RefreshAirbnbResolutionsBodyStatus(str, Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
