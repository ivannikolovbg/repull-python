from enum import Enum

class AccountCalendarAccessChangedEventEvent(str, Enum):
    ACCOUNT_CALENDAR_ACCESS_CHANGED = "account.calendar_access_changed"

    def __str__(self) -> str:
        return str(self.value)
