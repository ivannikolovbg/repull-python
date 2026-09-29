from enum import Enum

class WithdrawConversationPreapprovalResponse200Status(str, Enum):
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
