from enum import Enum

class GetVrboReservationOptions(str, Enum):
    CANCEL = "cancel"
    CHANGE = "change"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
