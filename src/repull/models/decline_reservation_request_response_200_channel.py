from enum import Enum

class DeclineReservationRequestResponse200Channel(str, Enum):
    AIRBNB = "airbnb"

    def __str__(self) -> str:
        return str(self.value)
