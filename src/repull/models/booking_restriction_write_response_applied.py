from enum import Enum

class BookingRestrictionWriteResponseApplied(str, Enum):
    ACKNOWLEDGED = "acknowledged"
    MISMATCH = "mismatch"
    REJECTED = "rejected"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
