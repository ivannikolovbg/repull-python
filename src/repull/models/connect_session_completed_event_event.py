from enum import Enum

class ConnectSessionCompletedEventEvent(str, Enum):
    CONNECT_SESSION_COMPLETED = "connect.session.completed"

    def __str__(self) -> str:
        return str(self.value)
