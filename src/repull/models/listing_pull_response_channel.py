from enum import Enum

class ListingPullResponseChannel(str, Enum):
    AIRBNB = "airbnb"

    def __str__(self) -> str:
        return str(self.value)
