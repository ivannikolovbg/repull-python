from enum import Enum

class ListingPublishStatusConnectionChannelStatusType3Type1(str, Enum):
    NOT_LIVE = "not_live"
    OFFLINE = "offline"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
