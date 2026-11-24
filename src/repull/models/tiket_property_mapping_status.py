from enum import Enum

class TiketPropertyMappingStatus(str, Enum):
    MAPPED = "mapped"
    PARTIAL = "partial"
    UNMAPPED = "unmapped"

    def __str__(self) -> str:
        return str(self.value)
