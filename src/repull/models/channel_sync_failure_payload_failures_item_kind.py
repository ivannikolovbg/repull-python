from enum import Enum

class ChannelSyncFailurePayloadFailuresItemKind(str, Enum):
    AUTH = "auth"
    NOT_MAPPED = "not_mapped"
    REJECTED = "rejected"
    UNKNOWN = "unknown"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
