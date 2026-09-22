from enum import Enum

class ListingSuspendedEventEvent(str, Enum):
    LISTING_SUSPENDED = "listing.suspended"

    def __str__(self) -> str:
        return str(self.value)
