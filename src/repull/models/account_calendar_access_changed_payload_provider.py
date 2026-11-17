from enum import Enum

class AccountCalendarAccessChangedPayloadProvider(str, Enum):
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
