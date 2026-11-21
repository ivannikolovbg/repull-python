from enum import Enum

class GetVrboListingFeesResponse200DataFreshnessReason(str, Enum):
    OK = "ok"
    RECONNECT_REQUIRED = "reconnect_required"
    REFRESHING = "refreshing"

    def __str__(self) -> str:
        return str(self.value)
