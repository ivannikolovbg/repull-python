from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CreateAirbnbListingRoomBodyBedsItem")



@_attrs_define
class CreateAirbnbListingRoomBodyBedsItem:
    """ 
        Attributes:
            type_ (str): Airbnb bed type, lowercase snake_case. Seen on live listings: king_bed, queen_bed, double_bed,
                small_double_bed, single_bed, bunk_bed, sofa_bed, couch, air_mattress, floor_mattress, toddler_bed, crib,
                hammock. Not a closed enum here — Airbnb's vocabulary drifts, so an unknown type is refused by Airbnb with its
                own message rather than by us.
            quantity (int):
     """

    type_: str
    quantity: int





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        quantity = self.quantity


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "quantity": quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        quantity = d.pop("quantity")

        create_airbnb_listing_room_body_beds_item = cls(
            type_=type_,
            quantity=quantity,
        )

        return create_airbnb_listing_room_body_beds_item

