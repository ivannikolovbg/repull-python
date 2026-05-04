from enum import Enum

class CalendarUpdatedEventType(str, Enum):
    CALENDAR_UPDATED = "calendar.updated"

    def __str__(self) -> str:
        return str(self.value)
