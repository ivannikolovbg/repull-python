from enum import Enum

class GetBookingContentType(str, Enum):
    CHECKIN_METHODS = "checkin_methods"
    CONTACTS = "contacts"
    DESCRIPTION = "description"
    FACILITIES = "facilities"
    LICENCES = "licences"
    PHOTOS = "photos"
    POLICIES = "policies"
    SETTINGS = "settings"

    def __str__(self) -> str:
        return str(self.value)
