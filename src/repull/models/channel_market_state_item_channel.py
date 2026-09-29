from enum import Enum

class ChannelMarketStateItemChannel(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
