from enum import Enum

class GetListingIcalResponse200CalendarName(str, Enum):
    REPULL = "Repull"

    def __str__(self) -> str:
        return str(self.value)
