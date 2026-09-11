from enum import Enum

class SendMessageResponseDirection(str, Enum):
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)
