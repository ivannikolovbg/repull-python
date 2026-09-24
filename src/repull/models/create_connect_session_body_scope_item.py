from enum import Enum

class CreateConnectSessionBodyScopeItem(str, Enum):
    AMENITIES = "amenities"
    CALENDAR = "calendar"
    CHANNELIDS = "channelIds"
    CONVERSATIONS = "conversations"
    FEES = "fees"
    GUESTS = "guests"
    HOUSERULES = "houseRules"
    LISTINGS = "listings"
    OWNERS = "owners"
    PAYMENTS = "payments"
    PHOTOS = "photos"
    RATES = "rates"
    RESERVATIONS = "reservations"
    ROOMS = "rooms"
    TAXES = "taxes"

    def __str__(self) -> str:
        return str(self.value)
