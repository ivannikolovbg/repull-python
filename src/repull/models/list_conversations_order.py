from enum import Enum

class ListConversationsOrder(str, Enum):
    CREATED = "created"
    RECENT = "recent"

    def __str__(self) -> str:
        return str(self.value)
