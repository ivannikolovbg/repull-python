from enum import Enum

class ReservationMessageSentPayloadSource(str, Enum):
    CHANNEL = "channel"
    REPULL = "repull"

    def __str__(self) -> str:
        return str(self.value)
