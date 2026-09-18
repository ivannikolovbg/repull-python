from enum import Enum

class ListAirbnbListingPermitsSource(str, Enum):
    CACHE = "cache"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
