from enum import Enum

class ListingIcalFeedChangedEventEvent(str, Enum):
    LISTING_ICAL_FEED_CHANGED = "listing.ical_feed_changed"

    def __str__(self) -> str:
        return str(self.value)
