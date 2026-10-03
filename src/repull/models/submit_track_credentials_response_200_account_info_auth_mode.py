from enum import Enum

class SubmitTrackCredentialsResponse200AccountInfoAuthMode(str, Enum):
    BASIC = "basic"
    HMAC = "hmac"

    def __str__(self) -> str:
        return str(self.value)
