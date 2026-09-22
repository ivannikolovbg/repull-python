from enum import Enum

class AirbnbReservationActionBodyReason(str, Enum):
    CALENDAR_CONFLICT = "calendar_conflict"
    DATES_NOT_AVAILABLE = "dates_not_available"
    DIFFERENT_DATES_NEEDED = "different_dates_needed"
    LISTING_NOT_READY = "listing_not_ready"
    MAINTENANCE_ISSUE = "maintenance_issue"
    NOT_COMFORTABLE = "not_comfortable"
    OTHER = "other"
    SPAM = "spam"
    UNABLE_TO_HOST = "unable_to_host"

    def __str__(self) -> str:
        return str(self.value)
