from enum import Enum

class PreapproveConversationResponse201Channel(str, Enum):
    AIRBNB = "airbnb"
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
