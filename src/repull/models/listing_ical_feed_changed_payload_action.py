from enum import Enum

class ListingIcalFeedChangedPayloadAction(str, Enum):
    OTHER_FEED_REMOVED = "other_feed_removed"
    OTHER_FEED_REMOVE_FAILED = "other_feed_remove_failed"
    REPULL_FEED_ADDED = "repull_feed_added"
    REPULL_FEED_ADD_FAILED = "repull_feed_add_failed"

    def __str__(self) -> str:
        return str(self.value)
