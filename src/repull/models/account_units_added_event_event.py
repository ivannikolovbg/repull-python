from enum import Enum

class AccountUnitsAddedEventEvent(str, Enum):
    ACCOUNT_UNITS_ADDED = "account.units.added"

    def __str__(self) -> str:
        return str(self.value)
