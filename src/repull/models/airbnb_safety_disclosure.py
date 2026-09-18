from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_safety_disclosure_type import AirbnbSafetyDisclosureType
from ..types import UNSET, Unset






T = TypeVar("T", bound="AirbnbSafetyDisclosure")



@_attrs_define
class AirbnbSafetyDisclosure:
    """ 
        Attributes:
            type_ (AirbnbSafetyDisclosureType): What is being disclosed. `surveillance` = exterior security cameras or
                recording devices. `noise_monitor` = a decibel monitor is installed. `requires_stairs`, `potential_noise`,
                `animals` (farm or wild animals nearby), `has_pets` (the host's pets), `limited_parking`, `limited_amenities`,
                `shared_spaces`, `pool_or_jacuzzi_with_no_fence`, `heights_with_no_fence`, `climbing_or_play_structure`,
                `lake_or_river_or_water_body`, `weapons`.
            value (bool): Whether it applies to this property.
            declared (bool | Unset): Read only: whether Airbnb holds an explicit answer for this type on this listing (as
                opposed to it simply not being declared).
     """

    type_: AirbnbSafetyDisclosureType
    value: bool
    declared: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        declared = self.declared


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "value": value,
        })
        if declared is not UNSET:
            field_dict["declared"] = declared

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AirbnbSafetyDisclosureType(d.pop("type"))




        value = d.pop("value")

        declared = d.pop("declared", UNSET)

        airbnb_safety_disclosure = cls(
            type_=type_,
            value=value,
            declared=declared,
        )


        airbnb_safety_disclosure.additional_properties = d
        return airbnb_safety_disclosure

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
