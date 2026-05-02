from enum import Enum

class ListingGenerateContentRequestStyle(str, Enum):
    CONCISE = "concise"
    PROFESSIONAL = "professional"
    WARM = "warm"

    def __str__(self) -> str:
        return str(self.value)
