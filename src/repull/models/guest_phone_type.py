from enum import Enum

class GuestPhoneType(str, Enum):
    AIRBNB_RELAY = "airbnb_relay"
    GUEST = "guest"

    def __str__(self) -> str:
        return str(self.value)
