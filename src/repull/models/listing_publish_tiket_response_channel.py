from enum import Enum

class ListingPublishTiketResponseChannel(str, Enum):
    TIKET = "tiket"

    def __str__(self) -> str:
        return str(self.value)
