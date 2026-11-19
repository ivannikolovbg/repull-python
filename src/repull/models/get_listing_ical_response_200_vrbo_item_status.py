from enum import Enum

class GetListingIcalResponse200VrboItemStatus(str, Enum):
    FAILED = "failed"
    IMPORTED = "imported"
    NOT_IMPORTED = "not_imported"
    OFF = "off"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
