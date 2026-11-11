from enum import Enum

class ConnectSessionAbandonedPayloadStatus(str, Enum):
    AWAITING_ROOM_MAPPING = "awaiting_room_mapping"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
