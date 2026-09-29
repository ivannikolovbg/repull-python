from enum import Enum

class GetListingCalendarSyncResponse200ChannelsItemStatus(str, Enum):
    IN_SYNC = "in_sync"
    OFF = "off"
    PROBLEMS = "problems"

    def __str__(self) -> str:
        return str(self.value)
