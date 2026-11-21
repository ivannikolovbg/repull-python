from enum import Enum

class GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1(str, Enum):
    FULL_ACCESS = "full_access"
    MESSAGING = "messaging"

    def __str__(self) -> str:
        return str(self.value)
