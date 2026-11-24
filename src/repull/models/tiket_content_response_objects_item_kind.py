from enum import Enum

class TiketContentResponseObjectsItemKind(str, Enum):
    PROPERTY = "property"
    RATEPLAN = "rateplan"
    ROOM = "room"

    def __str__(self) -> str:
        return str(self.value)
