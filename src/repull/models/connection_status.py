from enum import Enum

class ConnectionStatus(str, Enum):
    ACTIVE = "active"
    DISCONNECTED = "disconnected"
    ERROR = "error"
    INACTIVE = "inactive"
    NEEDS_PERMISSIONS = "needs_permissions"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
