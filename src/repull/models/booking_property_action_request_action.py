from enum import Enum

class BookingPropertyActionRequestAction(str, Enum):
    CLOSE = "close"
    OPEN = "open"
    RELIST = "relist"
    UNLIST = "unlist"

    def __str__(self) -> str:
        return str(self.value)
