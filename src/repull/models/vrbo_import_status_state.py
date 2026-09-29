from enum import Enum

class VrboImportStatusState(str, Enum):
    IMPORTED = "imported"
    IMPORTING = "importing"
    IMPORTING_HISTORY = "importing_history"
    NOT_STARTED = "not_started"

    def __str__(self) -> str:
        return str(self.value)
