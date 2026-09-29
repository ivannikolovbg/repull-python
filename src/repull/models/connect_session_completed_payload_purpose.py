from enum import Enum

class ConnectSessionCompletedPayloadPurpose(str, Enum):
    CONNECT = "connect"
    MIGRATE = "migrate"

    def __str__(self) -> str:
        return str(self.value)
