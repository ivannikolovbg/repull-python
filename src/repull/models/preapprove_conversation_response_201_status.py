from enum import Enum

class PreapproveConversationResponse201Status(str, Enum):
    PRE_APPROVED = "pre_approved"

    def __str__(self) -> str:
        return str(self.value)
