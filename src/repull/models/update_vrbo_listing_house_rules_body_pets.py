from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingHouseRulesBodyPets")



@_attrs_define
class UpdateVrboListingHouseRulesBodyPets:
    """ 
        Attributes:
            allowed (bool | Unset):
            max_ (int | None | Unset):
            allowed_pets (list[str] | None | str | Unset):
            max_weight (float | None | str | Unset):
            note (None | str | Unset):
     """

    allowed: bool | Unset = UNSET
    max_: int | None | Unset = UNSET
    allowed_pets: list[str] | None | str | Unset = UNSET
    max_weight: float | None | str | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        allowed_pets: list[str] | None | str | Unset
        if isinstance(self.allowed_pets, Unset):
            allowed_pets = UNSET
        elif isinstance(self.allowed_pets, list):
            allowed_pets = self.allowed_pets


        else:
            allowed_pets = self.allowed_pets

        max_weight: float | None | str | Unset
        if isinstance(self.max_weight, Unset):
            max_weight = UNSET
        else:
            max_weight = self.max_weight

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
        if max_ is not UNSET:
            field_dict["max"] = max_
        if allowed_pets is not UNSET:
            field_dict["allowedPets"] = allowed_pets
        if max_weight is not UNSET:
            field_dict["maxWeight"] = max_weight
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = d.pop("allowed", UNSET)

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))


        def _parse_allowed_pets(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_pets_type_1 = cast(list[str], data)

                return allowed_pets_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        allowed_pets = _parse_allowed_pets(d.pop("allowedPets", UNSET))


        def _parse_max_weight(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        max_weight = _parse_max_weight(d.pop("maxWeight", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        update_vrbo_listing_house_rules_body_pets = cls(
            allowed=allowed,
            max_=max_,
            allowed_pets=allowed_pets,
            max_weight=max_weight,
            note=note,
        )

        return update_vrbo_listing_house_rules_body_pets

