from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_response_200_data_freshness import GetVrboListingResponse200DataFreshness
  from ..models.get_vrbo_listing_response_200_data_item import GetVrboListingResponse200DataItem





T = TypeVar("T", bound="GetVrboListingResponse200")



@_attrs_define
class GetVrboListingResponse200:
    """ 
        Attributes:
            data (list[GetVrboListingResponse200DataItem]):
            data_freshness (GetVrboListingResponse200DataFreshness | Unset): Whether the Vrbo accounts are in sync — the
                same envelope as the Airbnb reads.
     """

    data: list[GetVrboListingResponse200DataItem]
    data_freshness: GetVrboListingResponse200DataFreshness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_response_200_data_freshness import GetVrboListingResponse200DataFreshness
        from ..models.get_vrbo_listing_response_200_data_item import GetVrboListingResponse200DataItem
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        data_freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })
        if data_freshness is not UNSET:
            field_dict["dataFreshness"] = data_freshness

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_response_200_data_freshness import GetVrboListingResponse200DataFreshness
        from ..models.get_vrbo_listing_response_200_data_item import GetVrboListingResponse200DataItem
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = GetVrboListingResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        _data_freshness = d.pop("dataFreshness", UNSET)
        data_freshness: GetVrboListingResponse200DataFreshness | Unset
        if isinstance(_data_freshness,  Unset):
            data_freshness = UNSET
        else:
            data_freshness = GetVrboListingResponse200DataFreshness.from_dict(_data_freshness)




        get_vrbo_listing_response_200 = cls(
            data=data,
            data_freshness=data_freshness,
        )


        get_vrbo_listing_response_200.additional_properties = d
        return get_vrbo_listing_response_200

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
