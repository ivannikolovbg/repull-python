from enum import Enum

class StartConnectionImportBodyScope(str, Enum):
    LISTINGS = "listings"

    def __str__(self) -> str:
        return str(self.value)
