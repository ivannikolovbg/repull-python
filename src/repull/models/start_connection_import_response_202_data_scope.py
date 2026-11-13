from enum import Enum

class StartConnectionImportResponse202DataScope(str, Enum):
    LISTINGS = "listings"

    def __str__(self) -> str:
        return str(self.value)
