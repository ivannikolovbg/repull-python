from enum import Enum

class WebhookEventCatalogEntryDomain(str, Enum):
    ACCOUNTS = "accounts"
    AI = "ai"
    CALENDAR = "calendar"
    LISTINGS = "listings"
    PAYMENTS = "payments"
    RESERVATIONS = "reservations"
    REVIEWS = "reviews"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
