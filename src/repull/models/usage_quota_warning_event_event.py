from enum import Enum

class UsageQuotaWarningEventEvent(str, Enum):
    USAGE_QUOTA_WARNING = "usage.quota.warning"

    def __str__(self) -> str:
        return str(self.value)
