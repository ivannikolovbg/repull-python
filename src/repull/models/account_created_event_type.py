from enum import Enum

class AccountCreatedEventType(str, Enum):
    ACCOUNT_CREATED = "account.created"

    def __str__(self) -> str:
        return str(self.value)
