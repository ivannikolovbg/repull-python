from enum import Enum

class ConversationMessageStatusChangedEventEvent(str, Enum):
    CONVERSATION_MESSAGE_STATUS_CHANGED = "conversation.message.status_changed"

    def __str__(self) -> str:
        return str(self.value)
