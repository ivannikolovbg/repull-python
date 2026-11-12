from enum import Enum

class AvailabilityWriteResultSyncedChannelsItemStatus(str, Enum):
    ACCEPTED = "accepted"
    FAILED = "failed"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
