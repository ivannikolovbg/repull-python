from enum import Enum

class SendMessageRequestChannel(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    EMAIL = "email"
    SMS = "sms"
    VRBO = "vrbo"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
