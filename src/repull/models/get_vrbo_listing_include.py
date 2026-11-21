from enum import Enum

class GetVrboListingInclude(str, Enum):
    CONTENT = "content"

    def __str__(self) -> str:
        return str(self.value)
