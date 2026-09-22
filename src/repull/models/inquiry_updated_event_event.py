from enum import Enum

class InquiryUpdatedEventEvent(str, Enum):
    INQUIRY_UPDATED = "inquiry.updated"

    def __str__(self) -> str:
        return str(self.value)
