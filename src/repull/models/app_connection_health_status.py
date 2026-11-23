from enum import Enum

class AppConnectionHealthStatus(str, Enum):
    ACTIVE = "active"
    FAILING = "failing"
    IDLE = "idle"
    NEVER_CONNECTED = "never_connected"

    def __str__(self) -> str:
        return str(self.value)
