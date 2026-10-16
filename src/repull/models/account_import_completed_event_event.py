from enum import Enum

class AccountImportCompletedEventEvent(str, Enum):
    ACCOUNT_IMPORT_COMPLETED = "account.import.completed"

    def __str__(self) -> str:
        return str(self.value)
