from enum import Enum

class GetVrboConnectionResponse200DataStatus(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    NEVER_CONNECTED = "never_connected"
    RECONNECT_REQUIRED = "reconnect_required"

    def __str__(self) -> str:
        return str(self.value)
