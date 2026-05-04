from enum import Enum

class PaymentRefundedEventType(str, Enum):
    PAYMENT_REFUNDED = "payment.refunded"

    def __str__(self) -> str:
        return str(self.value)
