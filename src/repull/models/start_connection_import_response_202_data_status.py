from enum import Enum

class StartConnectionImportResponse202DataStatus(str, Enum):
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
