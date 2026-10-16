from enum import Enum

class GetTransactionStatementFormat(str, Enum):
    CSV = "csv"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
