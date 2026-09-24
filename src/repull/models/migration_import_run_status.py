from enum import Enum

class MigrationImportRunStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
