from enum import Enum

class AccountImportStartedPayloadTrigger(str, Enum):
    CONNECT = "connect"
    MAPPING = "mapping"
    RECONNECT = "reconnect"
    RESYNC = "resync"

    def __str__(self) -> str:
        return str(self.value)
