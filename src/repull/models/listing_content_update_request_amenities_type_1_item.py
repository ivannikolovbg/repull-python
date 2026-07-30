from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateRequestAmenitiesType1Item")



@_attrs_define
class ListingContentUpdateRequestAmenitiesType1Item:
    """ 
        Attributes:
            amenity_key (str):
            category (None | str | Unset):
            is_present (bool | None | Unset):  Default: True.
            instruction (None | str | Unset):
     """

    amenity_key: str
    category: None | str | Unset = UNSET
    is_present: bool | None | Unset = True
    instruction: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amenity_key = self.amenity_key

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_present: bool | None | Unset
        if isinstance(self.is_present, Unset):
            is_present = UNSET
        else:
            is_present = self.is_present

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amenityKey": amenity_key,
        })
        if category is not UNSET:
            field_dict["category"] = category
        if is_present is not UNSET:
            field_dict["isPresent"] = is_present
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amenity_key = d.pop("amenityKey")

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_is_present(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_present = _parse_is_present(d.pop("isPresent", UNSET))


        def _parse_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instruction = _parse_instruction(d.pop("instruction", UNSET))


        listing_content_update_request_amenities_type_1_item = cls(
            amenity_key=amenity_key,
            category=category,
            is_present=is_present,
            instruction=instruction,
        )


        listing_content_update_request_amenities_type_1_item.additional_properties = d
        return listing_content_update_request_amenities_type_1_item

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
