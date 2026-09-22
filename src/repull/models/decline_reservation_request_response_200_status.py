from enum import Enum

class DeclineReservationRequestResponse200Status(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
