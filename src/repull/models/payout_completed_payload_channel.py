from enum import Enum

class PayoutCompletedPayloadChannel(str, Enum):
    AIRBNB = "airbnb"

    def __str__(self) -> str:
        return str(self.value)
