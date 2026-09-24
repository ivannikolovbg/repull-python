from enum import Enum

class MigrationFailedEventEvent(str, Enum):
    MIGRATION_FAILED = "migration.failed"

    def __str__(self) -> str:
        return str(self.value)
