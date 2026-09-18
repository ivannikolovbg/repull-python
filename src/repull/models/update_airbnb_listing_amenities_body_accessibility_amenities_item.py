from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem")



@_attrs_define
class UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem:
    """ 
        Attributes:
            id (str):
            is_present (bool):
            instruction (None | str | Unset):
            photo_ids (list[str] | Unset): Airbnb photo ids evidencing the accessibility claim (`photoAirbnbId` from `GET
                /photos`).
     """

    id: str
    is_present: bool
    instruction: None | str | Unset = UNSET
    photo_ids: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_present = self.is_present

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction

        photo_ids: list[str] | Unset = UNSET
        if not isinstance(self.photo_ids, Unset):
            photo_ids = self.photo_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "is_present": is_present,
        })
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if photo_ids is not UNSET:
            field_dict["photo_ids"] = photo_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_present = d.pop("is_present")

        def _parse_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instruction = _parse_instruction(d.pop("instruction", UNSET))


        photo_ids = cast(list[str], d.pop("photo_ids", UNSET))


        update_airbnb_listing_amenities_body_accessibility_amenities_item = cls(
            id=id,
            is_present=is_present,
            instruction=instruction,
            photo_ids=photo_ids,
        )

        return update_airbnb_listing_amenities_body_accessibility_amenities_item

