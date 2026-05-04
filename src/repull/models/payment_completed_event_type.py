from enum import Enum

class PaymentCompletedEventType(str, Enum):
    PAYMENT_COMPLETED = "payment.completed"

    def __str__(self) -> str:
        return str(self.value)
