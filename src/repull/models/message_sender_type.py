from enum import Enum

class MessageSenderType(str, Enum):
    GUEST = "guest"
    HOST = "host"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
