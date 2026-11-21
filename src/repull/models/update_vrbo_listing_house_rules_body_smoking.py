from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingHouseRulesBodySmoking")



@_attrs_define
class UpdateVrboListingHouseRulesBodySmoking:
    """ 
        Attributes:
            allowed (bool | Unset):
            inside (bool | None | Unset):
            outside (bool | None | Unset):
            note (None | str | Unset):
     """

    allowed: bool | Unset = UNSET
    inside: bool | None | Unset = UNSET
    outside: bool | None | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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
        allowed = d.pop("allowed", UNSET)

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


        update_vrbo_listing_house_rules_body_smoking = cls(
            allowed=allowed,
            inside=inside,
            outside=outside,
            note=note,
        )

        return update_vrbo_listing_house_rules_body_smoking

