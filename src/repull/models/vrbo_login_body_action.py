from enum import Enum

class VrboLoginBodyAction(str, Enum):
    LOGIN = "login"
    OTP = "otp"
    PHONE = "phone"
    RESEND = "resend"

    def __str__(self) -> str:
        return str(self.value)
