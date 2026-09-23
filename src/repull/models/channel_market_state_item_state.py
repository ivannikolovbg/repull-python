from enum import Enum

class ChannelMarketStateItemState(str, Enum):
    OFFLINE = "offline"
    ONLINE = "online"
    UNCHANGED = "unchanged"

    def __str__(self) -> str:
        return str(self.value)
