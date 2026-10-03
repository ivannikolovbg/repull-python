from enum import Enum

class ResumeConnectResponse500Error(str, Enum):
    INTERNAL_ERROR = "internal_error"

    def __str__(self) -> str:
        return str(self.value)
