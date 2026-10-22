from enum import Enum

class MessageStatus(str, Enum):
    FAILED = "failed"
    RECEIVED = "received"
    SENDING = "sending"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
