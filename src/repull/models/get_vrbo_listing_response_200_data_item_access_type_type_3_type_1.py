from enum import Enum

class GetVrboListingResponse200DataItemAccessTypeType3Type1(str, Enum):
    FULL_ACCESS = "full_access"
    MESSAGING = "messaging"

    def __str__(self) -> str:
        return str(self.value)
