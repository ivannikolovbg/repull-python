from enum import Enum

class GetListingCalendarSyncResponse200ChannelsItemOffReason(str, Enum):
    CALENDAR_MANAGED_ELSEWHERE = "calendar_managed_elsewhere"

    def __str__(self) -> str:
        return str(self.value)
