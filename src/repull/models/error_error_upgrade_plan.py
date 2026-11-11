from enum import Enum

class ErrorErrorUpgradePlan(str, Enum):
    CUSTOM = "custom"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
