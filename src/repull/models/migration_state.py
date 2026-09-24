from enum import Enum

class MigrationState(str, Enum):
    AWAITING_CONNECTION = "awaiting_connection"
    CUT_OVER = "cut_over"
    DEACTIVATED = "deactivated"
    FAILED = "failed"
    IMPORTED = "imported"
    IMPORTING = "importing"

    def __str__(self) -> str:
        return str(self.value)
