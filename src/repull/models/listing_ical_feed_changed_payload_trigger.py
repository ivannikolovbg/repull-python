from enum import Enum

class ListingIcalFeedChangedPayloadTrigger(str, Enum):
    CALENDAR_SYNC_ENABLED = "calendar_sync_enabled"
    DRIFT_CHECK = "drift_check"

    def __str__(self) -> str:
        return str(self.value)
