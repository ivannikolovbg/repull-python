from enum import Enum

class DeclineReservationRequestBodyReason(str, Enum):
    DATES_NOT_AVAILABLE = "dates_not_available"
    DIFFERENT_DATES_NEEDED = "different_dates_needed"
    LISTING_NOT_READY = "listing_not_ready"
    NOT_COMFORTABLE = "not_comfortable"
    OTHER = "other"
    SPAM = "spam"

    def __str__(self) -> str:
        return str(self.value)
