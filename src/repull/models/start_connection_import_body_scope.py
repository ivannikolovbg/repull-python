from enum import Enum

class StartConnectionImportBodyScope(str, Enum):
    FULL = "full"
    LISTINGS = "listings"

    def __str__(self) -> str:
        return str(self.value)
