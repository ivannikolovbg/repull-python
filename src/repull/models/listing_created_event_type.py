from enum import Enum

class ListingCreatedEventType(str, Enum):
    LISTING_CREATED = "listing.created"

    def __str__(self) -> str:
        return str(self.value)
