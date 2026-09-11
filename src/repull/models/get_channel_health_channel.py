from enum import Enum

class GetChannelHealthChannel(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    PLUMGUIDE = "plumguide"
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
