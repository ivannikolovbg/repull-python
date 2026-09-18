from enum import Enum

class AirbnbListingActionRequestAction(str, Enum):
    DELETE = "delete"
    PUBLISH = "publish"
    PUSH = "push"
    RELIST = "relist"
    UNLIST = "unlist"

    def __str__(self) -> str:
        return str(self.value)
