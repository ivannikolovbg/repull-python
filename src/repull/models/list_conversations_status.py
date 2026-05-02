from enum import Enum

class ListConversationsStatus(str, Enum):
    ARCHIVED = "archived"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
