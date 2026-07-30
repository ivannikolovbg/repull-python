from enum import Enum

class ListingContentUpdateRequestPhotosMode(str, Enum):
    APPEND = "append"
    REPLACE = "replace"

    def __str__(self) -> str:
        return str(self.value)
