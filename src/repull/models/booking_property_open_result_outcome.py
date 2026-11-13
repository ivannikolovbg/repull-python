from enum import Enum

class BookingPropertyOpenResultOutcome(str, Enum):
    FAILED = "failed"
    LISTING_INACTIVE = "listing_inactive"
    NOT_NEEDED = "not_needed"
    NO_LISTING = "no_listing"
    OPENED = "opened"
    REFUSED = "refused"

    def __str__(self) -> str:
        return str(self.value)
