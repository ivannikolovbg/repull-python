from enum import Enum

class PromotionChannel(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"

    def __str__(self) -> str:
        return str(self.value)
