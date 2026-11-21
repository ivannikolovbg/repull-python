from enum import Enum

class GetVrboConnectionResponse200DataAccountsItemStatus(str, Enum):
    CONNECTED = "connected"
    RECONNECT_REQUIRED = "reconnect_required"

    def __str__(self) -> str:
        return str(self.value)
