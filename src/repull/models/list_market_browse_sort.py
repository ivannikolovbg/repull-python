from enum import Enum

class ListMarketBrowseSort(str, Enum):
    LISTINGS_DESC = "listings_desc"
    NAME_ASC = "name_asc"

    def __str__(self) -> str:
        return str(self.value)
