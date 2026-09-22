from enum import Enum

class ListingReactivatedEventEvent(str, Enum):
    LISTING_REACTIVATED = "listing.reactivated"

    def __str__(self) -> str:
        return str(self.value)
