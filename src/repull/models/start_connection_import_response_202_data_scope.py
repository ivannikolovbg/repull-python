from enum import Enum

class StartConnectionImportResponse202DataScope(str, Enum):
    FULL = "full"
    LISTINGS = "listings"
    RESERVATIONS = "reservations"

    def __str__(self) -> str:
        return str(self.value)
