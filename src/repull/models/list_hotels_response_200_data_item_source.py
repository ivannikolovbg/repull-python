from enum import Enum

class ListHotelsResponse200DataItemSource(str, Enum):
    BOOKING = "booking"
    PMS = "pms"

    def __str__(self) -> str:
        return str(self.value)
