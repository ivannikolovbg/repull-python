from enum import Enum

class ConnectSessionAbandonedEventEvent(str, Enum):
    CONNECT_SESSION_ABANDONED = "connect.session.abandoned"

    def __str__(self) -> str:
        return str(self.value)
