from enum import Enum

class SubmitVrboGuestReviewBodyCategoryRatingsItemCategory(str, Enum):
    CLEANLINESS = "cleanliness"
    COMMUNICATION = "communication"
    RESPECT_HOUSE_RULES = "respect_house_rules"

    def __str__(self) -> str:
        return str(self.value)
