from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbConnectionAccessibilityAmenitiesType0Item")



@_attrs_define
class AirbnbConnectionAccessibilityAmenitiesType0Item:
    """ 
        Attributes:
            id (str | Unset): Airbnb amenity id (e.g. `wheelchair_accessible`, `home_step_free_access`).
            is_present (bool | Unset):
            instruction (None | str | Unset):
     """

    id: str | Unset = UNSET
    is_present: bool | Unset = UNSET
    instruction: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_present = self.is_present

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_present is not UNSET:
            field_dict["is_present"] = is_present
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_present = d.pop("is_present", UNSET)

        def _parse_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instruction = _parse_instruction(d.pop("instruction", UNSET))


        airbnb_connection_accessibility_amenities_type_0_item = cls(
            id=id,
            is_present=is_present,
            instruction=instruction,
        )


        airbnb_connection_accessibility_amenities_type_0_item.additional_properties = d
        return airbnb_connection_accessibility_amenities_type_0_item

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
