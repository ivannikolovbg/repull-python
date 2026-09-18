from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ReorderAirbnbListingPhotosBody")



@_attrs_define
class ReorderAirbnbListingPhotosBody:
    """ 
        Attributes:
            photo_ids (list[str]): Airbnb photo ids (`photoAirbnbId` from `GET /photos`) in display order, first photo
                first. No duplicates; every id must be on this listing.
     """

    photo_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        photo_ids = self.photo_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "photo_ids": photo_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_ids = cast(list[str], d.pop("photo_ids"))


        reorder_airbnb_listing_photos_body = cls(
            photo_ids=photo_ids,
        )

        return reorder_airbnb_listing_photos_body

