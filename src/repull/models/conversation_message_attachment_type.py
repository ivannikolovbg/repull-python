from enum import Enum

class ConversationMessageAttachmentType(str, Enum):
    AUDIO = "audio"
    FILE = "file"
    IMAGE = "image"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
