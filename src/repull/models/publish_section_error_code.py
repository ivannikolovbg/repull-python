from enum import Enum

class PublishSectionErrorCode(str, Enum):
    LOCKED = "locked"
    NO_CONTENT = "no_content"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
