from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingHouseRulesResponse200DataPets")



@_attrs_define
class UpdateVrboListingHouseRulesResponse200DataPets:
    """ 
        Attributes:
            allowed (bool | None | Unset):
            max_ (int | None | Unset):
            allowed_pets (Any | Unset):
            max_weight (Any | Unset):
            note (None | str | Unset):
     """

    allowed: bool | None | Unset = UNSET
    max_: int | None | Unset = UNSET
    allowed_pets: Any | Unset = UNSET
    max_weight: Any | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed: bool | None | Unset
        if isinstance(self.allowed, Unset):
            allowed = UNSET
        else:
            allowed = self.allowed

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        allowed_pets = self.allowed_pets

        max_weight = self.max_weight

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
        def _parse_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allowed = _parse_allowed(d.pop("allowed", UNSET))


        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))


        allowed_pets = d.pop("allowedPets", UNSET)

        max_weight = d.pop("maxWeight", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        update_vrbo_listing_house_rules_response_200_data_pets = cls(
            allowed=allowed,
            max_=max_,
            allowed_pets=allowed_pets,
            max_weight=max_weight,
            note=note,
        )


        update_vrbo_listing_house_rules_response_200_data_pets.additional_properties = d
        return update_vrbo_listing_house_rules_response_200_data_pets

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
