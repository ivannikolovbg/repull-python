from enum import Enum

class ListListingsStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
