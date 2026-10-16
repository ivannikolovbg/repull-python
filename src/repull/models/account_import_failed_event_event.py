from enum import Enum

class AccountImportFailedEventEvent(str, Enum):
    ACCOUNT_IMPORT_FAILED = "account.import.failed"

    def __str__(self) -> str:
        return str(self.value)
