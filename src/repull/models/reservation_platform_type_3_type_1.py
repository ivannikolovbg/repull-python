from enum import Enum

class ReservationPlatformType3Type1(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    DIRECT = "direct"
    OTHER = "other"
    OWNER = "owner"
    TIKET = "tiket"
    VRBO = "vrbo"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
