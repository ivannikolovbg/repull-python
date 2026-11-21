from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingRoomBodyBedsItem")



@_attrs_define
class UpdateVrboListingRoomBodyBedsItem:
    """ 
        Attributes:
            type_ (str): Airbnb's bed words (king_bed, queen_bed, double_bed, single_bed, bunk_bed, sofa_bed, couch,
                toddler_bed, crib) or Vrbo's (KING_BED, FUTON, MURPHY_BED, …). Example: king_bed.
            quantity (int):
            size (str | Unset): Vrbo's size, for beds that come in several (BUNK_BED, SOFA_BED, FUTON, MURPHY_BED). Defaults
                to the usual one. Example: KING.
     """

    type_: str
    quantity: int
    size: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        quantity = self.quantity

        size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "quantity": quantity,
        })
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        quantity = d.pop("quantity")

        size = d.pop("size", UNSET)

        update_vrbo_listing_room_body_beds_item = cls(
            type_=type_,
            quantity=quantity,
            size=size,
        )

        return update_vrbo_listing_room_body_beds_item

