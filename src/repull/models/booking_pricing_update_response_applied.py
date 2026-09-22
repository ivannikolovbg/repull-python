from enum import Enum

class BookingPricingUpdateResponseApplied(str, Enum):
    MISMATCH = "mismatch"
    PARTIAL = "partial"
    REJECTED = "rejected"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
