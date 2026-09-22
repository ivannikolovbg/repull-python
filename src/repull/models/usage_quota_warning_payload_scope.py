from enum import Enum

class UsageQuotaWarningPayloadScope(str, Enum):
    DAILY_REQUESTS = "daily_requests"

    def __str__(self) -> str:
        return str(self.value)
