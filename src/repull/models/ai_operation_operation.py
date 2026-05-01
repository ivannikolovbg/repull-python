from enum import Enum

class AIOperationOperation(str, Enum):
    CLASSIFY_INTENT = "classify-intent"
    GENERATE_LISTING = "generate-listing"
    PRICE_SUGGESTION = "price-suggestion"
    RESPOND_TO_GUEST = "respond-to-guest"
    REVIEW_RESPONSE = "review-response"

    def __str__(self) -> str:
        return str(self.value)
