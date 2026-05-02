from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.market_browse_entry import MarketBrowseEntry
  from ..models.market_browse_pagination import MarketBrowsePagination





T = TypeVar("T", bound="MarketBrowseResponse")



@_attrs_define
class MarketBrowseResponse:
    """ 
        Attributes:
            data (list[MarketBrowseEntry] | Unset):
            pagination (MarketBrowsePagination | Unset):
     """

    data: list[MarketBrowseEntry] | Unset = UNSET
    pagination: MarketBrowsePagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_browse_entry import MarketBrowseEntry
        from ..models.market_browse_pagination import MarketBrowsePagination
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_browse_entry import MarketBrowseEntry
        from ..models.market_browse_pagination import MarketBrowsePagination
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[MarketBrowseEntry] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = MarketBrowseEntry.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: MarketBrowsePagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = MarketBrowsePagination.from_dict(_pagination)




        market_browse_response = cls(
            data=data,
            pagination=pagination,
        )


        market_browse_response.additional_properties = d
        return market_browse_response

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
