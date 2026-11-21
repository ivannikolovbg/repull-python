from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_listing_property_response_200_data_interior_size_unit import GetVrboListingPropertyResponse200DataInteriorSizeUnit
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingPropertyResponse200DataInteriorSize")



@_attrs_define
class GetVrboListingPropertyResponse200DataInteriorSize:
    """ 
        Attributes:
            value (float | None | Unset):
            unit (GetVrboListingPropertyResponse200DataInteriorSizeUnit | Unset):
     """

    value: float | None | Unset = UNSET
    unit: GetVrboListingPropertyResponse200DataInteriorSizeUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if value is not UNSET:
            field_dict["value"] = value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        _unit = d.pop("unit", UNSET)
        unit: GetVrboListingPropertyResponse200DataInteriorSizeUnit | Unset
        if isinstance(_unit,  Unset):
            unit = UNSET
        else:
            unit = GetVrboListingPropertyResponse200DataInteriorSizeUnit(_unit)




        get_vrbo_listing_property_response_200_data_interior_size = cls(
            value=value,
            unit=unit,
        )


        get_vrbo_listing_property_response_200_data_interior_size.additional_properties = d
        return get_vrbo_listing_property_response_200_data_interior_size

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
