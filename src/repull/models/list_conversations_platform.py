from enum import Enum

class ListConversationsPlatform(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    EMAIL = "email"
    VRBO = "vrbo"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
