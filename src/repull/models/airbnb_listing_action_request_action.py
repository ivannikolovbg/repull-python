from enum import Enum

class AirbnbListingActionRequestAction(str, Enum):
    DELETE = "delete"
    PUBLISH = "publish"
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)
