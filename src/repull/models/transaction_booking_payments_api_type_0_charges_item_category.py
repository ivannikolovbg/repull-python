from enum import Enum

class TransactionBookingPaymentsApiType0ChargesItemCategory(str, Enum):
    COMMISSION = "commission"
    FEE = "fee"
    OTHER = "other"
    PAYMENT_CHARGE = "payment_charge"
    TAX = "tax"
    VAT = "vat"
    VAT_ON_FEES = "vat_on_fees"

    def __str__(self) -> str:
        return str(self.value)
