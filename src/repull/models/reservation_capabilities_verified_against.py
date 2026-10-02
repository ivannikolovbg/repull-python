from enum import Enum

class ReservationCapabilitiesVerifiedAgainst(str, Enum):
    SANDBOX = "sandbox"
    VENDOR_DOCS = "vendor_docs"

    def __str__(self) -> str:
        return str(self.value)
