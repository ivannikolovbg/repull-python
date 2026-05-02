from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MarketDetailResponsePropertyTypeMixItem")



@_attrs_define
class MarketDetailResponsePropertyTypeMixItem:
    """ 
        Attributes:
            property_type (str | Unset):
            count (int | Unset):
            avg_rate (int | None | Unset):
     """

    property_type: str | Unset = UNSET
    count: int | Unset = UNSET
    avg_rate: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_type = self.property_type

        count = self.count

        avg_rate: int | None | Unset
        if isinstance(self.avg_rate, Unset):
            avg_rate = UNSET
        else:
            avg_rate = self.avg_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_type is not UNSET:
            field_dict["property_type"] = property_type
        if count is not UNSET:
            field_dict["count"] = count
        if avg_rate is not UNSET:
            field_dict["avg_rate"] = avg_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_type = d.pop("property_type", UNSET)

        count = d.pop("count", UNSET)

        def _parse_avg_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg_rate = _parse_avg_rate(d.pop("avg_rate", UNSET))


        market_detail_response_property_type_mix_item = cls(
            property_type=property_type,
            count=count,
            avg_rate=avg_rate,
        )


        market_detail_response_property_type_mix_item.additional_properties = d
        return market_detail_response_property_type_mix_item

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
