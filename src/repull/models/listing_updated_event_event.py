from enum import Enum

class ListingUpdatedEventEvent(str, Enum):
    LISTING_UPDATED = "listing.updated"

    def __str__(self) -> str:
        return str(self.value)
