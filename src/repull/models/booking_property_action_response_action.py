from enum import Enum

class BookingPropertyActionResponseAction(str, Enum):
    CLOSE = "close"
    OPEN = "open"
    RELIST = "relist"
    UNLIST = "unlist"

    def __str__(self) -> str:
        return str(self.value)
