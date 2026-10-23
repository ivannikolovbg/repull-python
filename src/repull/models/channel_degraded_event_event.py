from enum import Enum

class ChannelDegradedEventEvent(str, Enum):
    CHANNEL_DEGRADED = "channel.degraded"

    def __str__(self) -> str:
        return str(self.value)
