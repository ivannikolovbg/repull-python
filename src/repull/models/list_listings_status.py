from enum import Enum

class ListListingsStatus(str, Enum):
    ACTIVE = "active"
    ALL = "all"
    ARCHIVED = "archived"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
