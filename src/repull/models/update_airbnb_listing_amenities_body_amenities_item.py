from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbListingAmenitiesBodyAmenitiesItem")



@_attrs_define
class UpdateAirbnbListingAmenitiesBodyAmenitiesItem:
    """ 
        Attributes:
            id (str): Airbnb amenity id, e.g. `wireless_internet`. Case is ignored.
            is_present (bool): `true` claims the amenity, `false` removes it. Required — an amenity with no `is_present`
                would be a silent no-op.
            instruction (None | str | Unset): Optional host note shown with the amenity.
     """

    id: str
    is_present: bool
    instruction: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_present = self.is_present

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "is_present": is_present,
        })
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

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


        update_airbnb_listing_amenities_body_amenities_item = cls(
            id=id,
            is_present=is_present,
            instruction=instruction,
        )

        return update_airbnb_listing_amenities_body_amenities_item

