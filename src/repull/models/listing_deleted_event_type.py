from enum import Enum

class ListingDeletedEventType(str, Enum):
    LISTING_DELETED = "listing.deleted"

    def __str__(self) -> str:
        return str(self.value)
