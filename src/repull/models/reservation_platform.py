from enum import Enum

class ReservationPlatform(str, Enum):
    AIRBNB = "airbnb"
    BOOKING_COM = "booking.com"
    DIRECT = "direct"
    OTHER = "other"
    OWNER = "owner"
    VRBO = "vrbo"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
