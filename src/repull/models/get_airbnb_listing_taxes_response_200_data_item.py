from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_airbnb_listing_taxes_response_200_data_item_source import GetAirbnbListingTaxesResponse200DataItemSource
from ..types import UNSET, Unset






T = TypeVar("T", bound="GetAirbnbListingTaxesResponse200DataItem")



@_attrs_define
class GetAirbnbListingTaxesResponse200DataItem:
    """ 
        Attributes:
            source (GetAirbnbListingTaxesResponse200DataItemSource | Unset):
     """

    source: GetAirbnbListingTaxesResponse200DataItemSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: GetAirbnbListingTaxesResponse200DataItemSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GetAirbnbListingTaxesResponse200DataItemSource(_source)




        get_airbnb_listing_taxes_response_200_data_item = cls(
            source=source,
        )


        get_airbnb_listing_taxes_response_200_data_item.additional_properties = d
        return get_airbnb_listing_taxes_response_200_data_item

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
