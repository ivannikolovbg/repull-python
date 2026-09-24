from enum import Enum

class MigrationImportPayloadStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
