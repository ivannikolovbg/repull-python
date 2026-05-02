from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.market_top_comp import MarketTopComp





T = TypeVar("T", bound="MarketDetailResponseTopComps")



@_attrs_define
class MarketDetailResponseTopComps:
    """ 
        Attributes:
            items (list[MarketTopComp] | Unset):
            map_items (list[MarketTopComp] | Unset):
            total (int | Unset):
            page (int | Unset):
            page_size (int | Unset):
     """

    items: list[MarketTopComp] | Unset = UNSET
    map_items: list[MarketTopComp] | Unset = UNSET
    total: int | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_top_comp import MarketTopComp
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        map_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.map_items, Unset):
            map_items = []
            for map_items_item_data in self.map_items:
                map_items_item = map_items_item_data.to_dict()
                map_items.append(map_items_item)



        total = self.total

        page = self.page

        page_size = self.page_size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if map_items is not UNSET:
            field_dict["mapItems"] = map_items
        if total is not UNSET:
            field_dict["total"] = total
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_top_comp import MarketTopComp
        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[MarketTopComp] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = MarketTopComp.from_dict(items_item_data)



                items.append(items_item)


        _map_items = d.pop("mapItems", UNSET)
        map_items: list[MarketTopComp] | Unset = UNSET
        if _map_items is not UNSET:
            map_items = []
            for map_items_item_data in _map_items:
                map_items_item = MarketTopComp.from_dict(map_items_item_data)



                map_items.append(map_items_item)


        total = d.pop("total", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        market_detail_response_top_comps = cls(
            items=items,
            map_items=map_items,
            total=total,
            page=page,
            page_size=page_size,
        )


        market_detail_response_top_comps.additional_properties = d
        return market_detail_response_top_comps

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
