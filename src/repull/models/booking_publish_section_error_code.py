from enum import Enum

class BookingPublishSectionErrorCode(str, Enum):
    NO_CONTENT = "no_content"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
