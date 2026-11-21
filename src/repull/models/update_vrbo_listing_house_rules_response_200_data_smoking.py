from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingHouseRulesResponse200DataSmoking")



@_attrs_define
class UpdateVrboListingHouseRulesResponse200DataSmoking:
    """ 
        Attributes:
            allowed (bool | None | Unset):
            inside (bool | None | Unset):
            outside (bool | None | Unset):
            note (None | str | Unset):
     """

    allowed: bool | None | Unset = UNSET
    inside: bool | None | Unset = UNSET
    outside: bool | None | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed: bool | None | Unset
        if isinstance(self.allowed, Unset):
            allowed = UNSET
        else:
            allowed = self.allowed

        inside: bool | None | Unset
        if isinstance(self.inside, Unset):
            inside = UNSET
        else:
            inside = self.inside

        outside: bool | None | Unset
        if isinstance(self.outside, Unset):
            outside = UNSET
        else:
            outside = self.outside

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if inside is not UNSET:
            field_dict["inside"] = inside
        if outside is not UNSET:
            field_dict["outside"] = outside
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allowed = _parse_allowed(d.pop("allowed", UNSET))


        def _parse_inside(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inside = _parse_inside(d.pop("inside", UNSET))


        def _parse_outside(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        outside = _parse_outside(d.pop("outside", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        update_vrbo_listing_house_rules_response_200_data_smoking = cls(
            allowed=allowed,
            inside=inside,
            outside=outside,
            note=note,
        )


        update_vrbo_listing_house_rules_response_200_data_smoking.additional_properties = d
        return update_vrbo_listing_house_rules_response_200_data_smoking

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
