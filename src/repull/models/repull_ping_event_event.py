from enum import Enum

class RepullPingEventEvent(str, Enum):
    REPULL_PING = "repull.ping"

    def __str__(self) -> str:
        return str(self.value)
