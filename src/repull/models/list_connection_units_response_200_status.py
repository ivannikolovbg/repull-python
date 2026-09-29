from enum import Enum

class ListConnectionUnitsResponse200Status(str, Enum):
    COMPLETED = "completed"
    IMPORTING = "importing"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
