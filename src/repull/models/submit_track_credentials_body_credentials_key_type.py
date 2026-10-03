from enum import Enum

class SubmitTrackCredentialsBodyCredentialsKeyType(str, Enum):
    CHANNEL = "channel"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)
