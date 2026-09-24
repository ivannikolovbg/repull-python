from enum import Enum

class ConnectSessionPurpose(str, Enum):
    MIGRATE = "migrate"

    def __str__(self) -> str:
        return str(self.value)
