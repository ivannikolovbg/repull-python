from enum import Enum

class SetListingMarkupBodyChannel(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"

    def __str__(self) -> str:
        return str(self.value)
