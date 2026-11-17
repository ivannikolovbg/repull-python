from enum import Enum

class MessageStatus(str, Enum):
    FAILED = "failed"
    QUEUED = "queued"
    RECEIVED = "received"
    SENDING = "sending"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
