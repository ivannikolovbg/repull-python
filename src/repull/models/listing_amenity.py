from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingAmenity")



@_attrs_define
class ListingAmenity:
    """ A single amenity row from the unified `listings_amenities` table. Surfaced on `GET /v1/listings/{id}` and `GET
    /v1/properties/{id}` only when the caller passes `?include=amenities`.

        Attributes:
            amenity_key (str): Canonical amenity key (e.g. `wifi`, `pool`, `parking`). Example: wifi.
            is_present (bool): `true` when the listing has this amenity, `false` when it has been explicitly opted out.
            category (None | str | Unset): Optional grouping (e.g. `essentials`, `safety`).
            instruction (None | str | Unset): Optional free-form instruction for the guest (e.g. WiFi password, parking
                notes).
     """

    amenity_key: str
    is_present: bool
    category: None | str | Unset = UNSET
    instruction: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amenity_key = self.amenity_key

        is_present = self.is_present

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amenityKey": amenity_key,
            "isPresent": is_present,
        })
        if category is not UNSET:
            field_dict["category"] = category
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amenity_key = d.pop("amenityKey")

        is_present = d.pop("isPresent")

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instruction = _parse_instruction(d.pop("instruction", UNSET))


        listing_amenity = cls(
            amenity_key=amenity_key,
            is_present=is_present,
            category=category,
            instruction=instruction,
        )


        listing_amenity.additional_properties = d
        return listing_amenity

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
