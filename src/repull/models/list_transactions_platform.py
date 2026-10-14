from enum import Enum

class ListTransactionsPlatform(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
