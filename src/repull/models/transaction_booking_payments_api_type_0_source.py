from enum import Enum

class TransactionBookingPaymentsApiType0Source(str, Enum):
    PAYMENTS_API = "payments_api"

    def __str__(self) -> str:
        return str(self.value)
