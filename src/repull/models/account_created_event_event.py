from enum import Enum

class AccountCreatedEventEvent(str, Enum):
    ACCOUNT_CREATED = "account.created"

    def __str__(self) -> str:
        return str(self.value)
