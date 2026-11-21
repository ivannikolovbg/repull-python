from enum import Enum

class ListVrboTransactionsResponse200DataFreshnessReason(str, Enum):
    NEVER_SYNCED = "never_synced"
    OK = "ok"
    RECONNECT_REQUIRED = "reconnect_required"
    REFRESHING = "refreshing"

    def __str__(self) -> str:
        return str(self.value)
