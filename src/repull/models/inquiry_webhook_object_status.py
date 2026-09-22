from enum import Enum

class InquiryWebhookObjectStatus(str, Enum):
    BOOKED = "booked"
    DECLINED = "declined"
    EXPIRED = "expired"
    NOT_POSSIBLE = "not_possible"
    OPEN = "open"
    PRE_APPROVED = "pre_approved"
    SPECIAL_OFFER_SENT = "special_offer_sent"

    def __str__(self) -> str:
        return str(self.value)
