from enum import Enum

class VrboLoginBodyAction(str, Enum):
    LOGIN = "login"
    OTP = "otp"

    def __str__(self) -> str:
        return str(self.value)
