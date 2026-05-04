from enum import Enum

class AccountDisconnectedEventType(str, Enum):
    ACCOUNT_DISCONNECTED = "account.disconnected"

    def __str__(self) -> str:
        return str(self.value)
