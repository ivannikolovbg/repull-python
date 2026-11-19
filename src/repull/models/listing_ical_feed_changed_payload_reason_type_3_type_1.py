from enum import Enum

class ListingIcalFeedChangedPayloadReasonType3Type1(str, Enum):
    REPULL_FEED_MISSING = "repull_feed_missing"
    REPULL_IS_MASTER_CALENDAR = "repull_is_master_calendar"

    def __str__(self) -> str:
        return str(self.value)
