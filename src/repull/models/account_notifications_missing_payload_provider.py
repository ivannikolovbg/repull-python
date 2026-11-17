from enum import Enum

class AccountNotificationsMissingPayloadProvider(str, Enum):
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
