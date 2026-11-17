from enum import Enum

class VrboCalendarAccessManagedBy(str, Enum):
    INTEGRATED_SOFTWARE = "integrated_software"

    def __str__(self) -> str:
        return str(self.value)
