from enum import Enum

class GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0Result(str, Enum):
    IN_SYNC = "in_sync"
    PROBLEMS = "problems"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
