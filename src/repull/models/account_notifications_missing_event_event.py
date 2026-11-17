from enum import Enum

class AccountNotificationsMissingEventEvent(str, Enum):
    ACCOUNT_NOTIFICATIONS_MISSING = "account.notifications_missing"

    def __str__(self) -> str:
        return str(self.value)
