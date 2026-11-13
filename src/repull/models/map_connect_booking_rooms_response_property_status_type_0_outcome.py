from enum import Enum

class MapConnectBookingRoomsResponsePropertyStatusType0Outcome(str, Enum):
    BLOCKED = "blocked"
    FAILED = "failed"
    LISTING_INACTIVE = "listing_inactive"
    NOT_NEEDED = "not_needed"
    NO_LISTING = "no_listing"
    OPENED = "opened"
    STATUS_UNKNOWN = "status_unknown"

    def __str__(self) -> str:
        return str(self.value)
