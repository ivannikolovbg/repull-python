from enum import Enum

class ListingPublishStatusChannelPushStatus(str, Enum):
    ERROR = "error"
    IDLE = "idle"
    PUSHING = "pushing"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
