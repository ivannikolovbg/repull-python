from enum import Enum

class RunMigrationImportBodyEntitiesItem(str, Enum):
    CALENDAR = "calendar"
    LISTINGS = "listings"
    MESSAGES = "messages"
    RESERVATIONS = "reservations"

    def __str__(self) -> str:
        return str(self.value)
