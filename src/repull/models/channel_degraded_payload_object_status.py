from enum import Enum

class ChannelDegradedPayloadObjectStatus(str, Enum):
    DEGRADED = "degraded"
    DOWN = "down"

    def __str__(self) -> str:
        return str(self.value)
