from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_airbnb_thread_messages_response_200_data_freshness import ListAirbnbThreadMessagesResponse200DataFreshness
  from ..models.list_airbnb_thread_messages_response_200_data_item import ListAirbnbThreadMessagesResponse200DataItem
  from ..models.list_airbnb_thread_messages_response_200_pagination import ListAirbnbThreadMessagesResponse200Pagination





T = TypeVar("T", bound="ListAirbnbThreadMessagesResponse200")



@_attrs_define
class ListAirbnbThreadMessagesResponse200:
    """ 
        Attributes:
            data (list[ListAirbnbThreadMessagesResponse200DataItem] | Unset):
            pagination (ListAirbnbThreadMessagesResponse200Pagination | Unset): Absent when `?all=true`.
            data_freshness (ListAirbnbThreadMessagesResponse200DataFreshness | Unset): When this workspace's Airbnb data was
                last synced.
     """

    data: list[ListAirbnbThreadMessagesResponse200DataItem] | Unset = UNSET
    pagination: ListAirbnbThreadMessagesResponse200Pagination | Unset = UNSET
    data_freshness: ListAirbnbThreadMessagesResponse200DataFreshness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_airbnb_thread_messages_response_200_data_freshness import ListAirbnbThreadMessagesResponse200DataFreshness
        from ..models.list_airbnb_thread_messages_response_200_data_item import ListAirbnbThreadMessagesResponse200DataItem
        from ..models.list_airbnb_thread_messages_response_200_pagination import ListAirbnbThreadMessagesResponse200Pagination
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        data_freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if data_freshness is not UNSET:
            field_dict["dataFreshness"] = data_freshness

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_airbnb_thread_messages_response_200_data_freshness import ListAirbnbThreadMessagesResponse200DataFreshness
        from ..models.list_airbnb_thread_messages_response_200_data_item import ListAirbnbThreadMessagesResponse200DataItem
        from ..models.list_airbnb_thread_messages_response_200_pagination import ListAirbnbThreadMessagesResponse200Pagination
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ListAirbnbThreadMessagesResponse200DataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ListAirbnbThreadMessagesResponse200DataItem.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: ListAirbnbThreadMessagesResponse200Pagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = ListAirbnbThreadMessagesResponse200Pagination.from_dict(_pagination)




        _data_freshness = d.pop("dataFreshness", UNSET)
        data_freshness: ListAirbnbThreadMessagesResponse200DataFreshness | Unset
        if isinstance(_data_freshness,  Unset):
            data_freshness = UNSET
        else:
            data_freshness = ListAirbnbThreadMessagesResponse200DataFreshness.from_dict(_data_freshness)




        list_airbnb_thread_messages_response_200 = cls(
            data=data,
            pagination=pagination,
            data_freshness=data_freshness,
        )


        list_airbnb_thread_messages_response_200.additional_properties = d
        return list_airbnb_thread_messages_response_200

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
