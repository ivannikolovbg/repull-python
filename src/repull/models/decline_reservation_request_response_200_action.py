from enum import Enum

class DeclineReservationRequestResponse200Action(str, Enum):
    ACCEPT = "accept"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
