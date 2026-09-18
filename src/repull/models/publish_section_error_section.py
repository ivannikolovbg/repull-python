from enum import Enum

class PublishSectionErrorSection(str, Enum):
    AMENITIES = "amenities"
    CHECKOUT_TASKS = "checkout_tasks"
    DESCRIPTION = "description"
    DETAILS = "details"
    PHOTOS = "photos"
    POLICIES = "policies"
    PRICING = "pricing"
    ROOMS = "rooms"

    def __str__(self) -> str:
        return str(self.value)
