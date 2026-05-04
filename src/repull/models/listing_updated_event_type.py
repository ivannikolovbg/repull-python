from enum import Enum

class ListingUpdatedEventType(str, Enum):
    LISTING_UPDATED = "listing.updated"

    def __str__(self) -> str:
        return str(self.value)
