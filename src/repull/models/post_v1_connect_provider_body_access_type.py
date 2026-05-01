from enum import Enum

class PostV1ConnectProviderBodyAccessType(str, Enum):
    FULL_ACCESS = "full_access"
    READ_ONLY = "read_only"

    def __str__(self) -> str:
        return str(self.value)
