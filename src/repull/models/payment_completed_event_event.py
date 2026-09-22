from enum import Enum

class PaymentCompletedEventEvent(str, Enum):
    PAYMENT_COMPLETED = "payment.completed"

    def __str__(self) -> str:
        return str(self.value)
