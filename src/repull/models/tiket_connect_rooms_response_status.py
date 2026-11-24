from enum import Enum

class TiketConnectRoomsResponseStatus(str, Enum):
    COMPLETED = "completed"
    IMPORTING = "importing"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
