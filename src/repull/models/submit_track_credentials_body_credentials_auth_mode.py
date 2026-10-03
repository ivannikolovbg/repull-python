from enum import Enum

class SubmitTrackCredentialsBodyCredentialsAuthMode(str, Enum):
    BASIC = "basic"
    HMAC = "hmac"

    def __str__(self) -> str:
        return str(self.value)
