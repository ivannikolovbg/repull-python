from enum import Enum

class AirbnbListingLifecycleResponseChannel(str, Enum):
    AIRBNB = "airbnb"

    def __str__(self) -> str:
        return str(self.value)
