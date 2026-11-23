from enum import Enum

class GetPriceLabsSessionStatusResponse200Status(str, Enum):
    CONNECTED = "connected"
    EXPIRED = "expired"
    PENDING = "pending"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
