from enum import Enum

class ReservationMessageReceivedPayloadDirection(str, Enum):
    INBOUND = "inbound"

    def __str__(self) -> str:
        return str(self.value)
