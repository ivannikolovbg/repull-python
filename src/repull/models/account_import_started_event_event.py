from enum import Enum

class AccountImportStartedEventEvent(str, Enum):
    ACCOUNT_IMPORT_STARTED = "account.import.started"

    def __str__(self) -> str:
        return str(self.value)
