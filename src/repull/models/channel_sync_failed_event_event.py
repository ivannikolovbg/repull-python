from enum import Enum

class ChannelSyncFailedEventEvent(str, Enum):
    CHANNEL_SYNC_FAILED = "channel.sync.failed"

    def __str__(self) -> str:
        return str(self.value)
