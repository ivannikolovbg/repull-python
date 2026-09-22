from enum import Enum

class PaymentWebhookObjectTransactionType(str, Enum):
    ADJUSTMENT = "adjustment"
    CHARGE = "charge"
    OTHER = "other"
    PASS_THROUGH_TAX = "pass_through_tax"
    PAYOUT = "payout"
    REFUND = "refund"
    RESERVATION = "reservation"
    RESOLUTION_PAYOUT = "resolution_payout"

    def __str__(self) -> str:
        return str(self.value)
