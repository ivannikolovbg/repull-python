from enum import Enum

class ListingCreatedEventEvent(str, Enum):
    LISTING_CREATED = "listing.created"

    def __str__(self) -> str:
        return str(self.value)
