from enum import Enum

class AccountImportFinishedPayloadOutcome(str, Enum):
    COMPLETE = "complete"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
