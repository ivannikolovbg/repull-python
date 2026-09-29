from enum import Enum

class GetListingCalendarSyncResponse200ChannelsItemQueueState(str, Enum):
    IDLE = "idle"
    QUEUED = "queued"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
