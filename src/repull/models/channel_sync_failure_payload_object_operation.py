from enum import Enum

class ChannelSyncFailurePayloadObjectOperation(str, Enum):
    AVAILABILITY = "availability"
    CONTENT = "content"
    RATE = "rate"
    RESERVATION = "reservation"
    RESTRICTION = "restriction"

    def __str__(self) -> str:
        return str(self.value)
