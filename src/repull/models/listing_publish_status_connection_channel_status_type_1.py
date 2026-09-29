from enum import Enum

class ListingPublishStatusConnectionChannelStatusType1(str, Enum):
    NOT_LIVE = "not_live"
    OFFLINE = "offline"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
