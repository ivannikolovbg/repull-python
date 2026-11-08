from enum import Enum

class BookingDerivedPricingWriteResponseApplied(str, Enum):
    MISMATCH = "mismatch"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
