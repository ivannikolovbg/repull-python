from enum import Enum

class VrboLoginResponse200Status(str, Enum):
    CONNECTED = "connected"
    FAILED = "failed"
    OTP_REQUIRED = "otp_required"
    PENDING = "pending"
    PHONE_REQUIRED = "phone_required"

    def __str__(self) -> str:
        return str(self.value)
