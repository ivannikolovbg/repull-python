from enum import Enum

class ListingContentUpdateResponsePmsType0ErrorsItemCode(str, Enum):
    DUPLICATE = "duplicate"
    NOT_FOUND = "not_found"
    REAUTH_REQUIRED = "reauth_required"
    REJECTED = "rejected"
    UNAVAILABLE = "unavailable"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
