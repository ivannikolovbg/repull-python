from enum import Enum

class RepullPingEventType(str, Enum):
    REPULL_PING = "repull.ping"

    def __str__(self) -> str:
        return str(self.value)
