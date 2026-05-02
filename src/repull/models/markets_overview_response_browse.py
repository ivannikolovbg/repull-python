from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.market_browse_category import MarketBrowseCategory
  from ..models.market_browse_featured import MarketBrowseFeatured





T = TypeVar("T", bound="MarketsOverviewResponseBrowse")



@_attrs_define
class MarketsOverviewResponseBrowse:
    """ Lightweight discovery summary. Use `/v1/markets/browse` for the full paginated catalog.

        Attributes:
            featured (list[MarketBrowseFeatured] | Unset): Top ~50 markets by listing volume the customer doesn't already
                operate in.
            categories (list[MarketBrowseCategory] | Unset): Top 50 countries by tracked-city count.
            total_available (int | Unset): Total Atlas-tracked cities in the catalog.
     """

    featured: list[MarketBrowseFeatured] | Unset = UNSET
    categories: list[MarketBrowseCategory] | Unset = UNSET
    total_available: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_browse_category import MarketBrowseCategory
        from ..models.market_browse_featured import MarketBrowseFeatured
        featured: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.featured, Unset):
            featured = []
            for featured_item_data in self.featured:
                featured_item = featured_item_data.to_dict()
                featured.append(featured_item)



        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)



        total_available = self.total_available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if featured is not UNSET:
            field_dict["featured"] = featured
        if categories is not UNSET:
            field_dict["categories"] = categories
        if total_available is not UNSET:
            field_dict["total_available"] = total_available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_browse_category import MarketBrowseCategory
        from ..models.market_browse_featured import MarketBrowseFeatured
        d = dict(src_dict)
        _featured = d.pop("featured", UNSET)
        featured: list[MarketBrowseFeatured] | Unset = UNSET
        if _featured is not UNSET:
            featured = []
            for featured_item_data in _featured:
                featured_item = MarketBrowseFeatured.from_dict(featured_item_data)



                featured.append(featured_item)


        _categories = d.pop("categories", UNSET)
        categories: list[MarketBrowseCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = MarketBrowseCategory.from_dict(categories_item_data)



                categories.append(categories_item)


        total_available = d.pop("total_available", UNSET)

        markets_overview_response_browse = cls(
            featured=featured,
            categories=categories,
            total_available=total_available,
        )


        markets_overview_response_browse.additional_properties = d
        return markets_overview_response_browse

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
