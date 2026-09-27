from enum import Enum

class ReservationMessageSentPayloadDirection(str, Enum):
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)
