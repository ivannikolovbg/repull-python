from enum import Enum

class AirbnbListingLifecycleResponseAction(str, Enum):
    RELIST = "relist"
    UNLIST = "unlist"

    def __str__(self) -> str:
        return str(self.value)
