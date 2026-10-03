from enum import Enum

class ResumeConnectResponse400Error(str, Enum):
    BAD_ACCOUNT = "bad_account"
    INVALID_RESUME_TOKEN = "invalid_resume_token"
    UNSUPPORTED_CHANNEL = "unsupported_channel"

    def __str__(self) -> str:
        return str(self.value)
