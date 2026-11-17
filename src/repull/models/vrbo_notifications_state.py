from enum import Enum

class VrboNotificationsState(str, Enum):
    ACTIVE = "active"
    MISSING = "missing"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
