from enum import Enum

class ReservationCreateRequestPlatform(str, Enum):
    DIRECT = "direct"
    OWNER = "owner"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
