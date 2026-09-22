from enum import Enum

class AirbnbReservationActionBodyAction(str, Enum):
    ACCEPT = "accept"
    CANCEL = "cancel"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
