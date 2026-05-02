from enum import Enum

class BulkPricingFailureErrorCode(str, Enum):
    CALENDAR_UPDATE_FAILED = "calendar_update_failed"
    INTERNAL_ERROR = "internal_error"
    NOT_OWNED = "not_owned"
    NO_PENDING_RECOMMENDATIONS = "no_pending_recommendations"

    def __str__(self) -> str:
        return str(self.value)
