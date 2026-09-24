from enum import Enum

class MigrationCompletedEventEvent(str, Enum):
    MIGRATION_COMPLETED = "migration.completed"

    def __str__(self) -> str:
        return str(self.value)
