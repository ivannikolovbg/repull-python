from enum import Enum

class WithdrawConversationSpecialOfferResponse200Status(str, Enum):
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
