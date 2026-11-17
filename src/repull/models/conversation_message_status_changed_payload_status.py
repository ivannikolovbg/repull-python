from enum import Enum

class ConversationMessageStatusChangedPayloadStatus(str, Enum):
    FAILED = "failed"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
