from enum import Enum

class CreateConnectSessionBodyPurpose(str, Enum):
    CONNECT = "connect"
    MIGRATE = "migrate"

    def __str__(self) -> str:
        return str(self.value)
