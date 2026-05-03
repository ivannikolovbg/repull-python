from enum import Enum

class ListPropertiesStatus(str, Enum):
    ACTIVE = "active"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
