from enum import Enum

class BillingNoticeCode(str, Enum):
    PAYMENT_FAILED = "payment_failed"

    def __str__(self) -> str:
        return str(self.value)
