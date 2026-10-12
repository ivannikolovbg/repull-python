from enum import Enum

class CreateBillingCheckoutBodyPlan(str, Enum):
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
