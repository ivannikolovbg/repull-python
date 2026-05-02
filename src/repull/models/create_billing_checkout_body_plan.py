from enum import Enum

class CreateBillingCheckoutBodyPlan(str, Enum):
    GROWTH = "growth"
    SCALE = "scale"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
