from enum import Enum

class WorkspaceCreatedVia(str, Enum):
    CONNECT = "connect"
    MIGRATE = "migrate"

    def __str__(self) -> str:
        return str(self.value)
