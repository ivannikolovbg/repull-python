from enum import Enum

class InquiryCreatedEventEvent(str, Enum):
    INQUIRY_CREATED = "inquiry.created"

    def __str__(self) -> str:
        return str(self.value)
