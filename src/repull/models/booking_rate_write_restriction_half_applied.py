from enum import Enum

class BookingRateWriteRestrictionHalfApplied(str, Enum):
    MISMATCH = "mismatch"
    NOT_REQUESTED = "not_requested"
    REJECTED = "rejected"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
