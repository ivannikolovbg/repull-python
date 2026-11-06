from enum import Enum

class AirbnbAccessAccountsItemState(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    NEVER_CONNECTED = "never_connected"

    def __str__(self) -> str:
        return str(self.value)
