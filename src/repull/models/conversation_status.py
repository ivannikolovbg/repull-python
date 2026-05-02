from enum import Enum

class ConversationStatus(str, Enum):
    ARCHIVED = "archived"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
