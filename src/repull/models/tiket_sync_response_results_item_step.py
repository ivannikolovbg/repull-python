from enum import Enum

class TiketSyncResponseResultsItemStep(str, Enum):
    CALENDAR = "calendar"
    REFRESH_PRODUCTS = "refresh_products"

    def __str__(self) -> str:
        return str(self.value)
