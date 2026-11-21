from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingPhotoBody")



@_attrs_define
class UpdateVrboListingPhotoBody:
    """ 
        Attributes:
            photo_id (str):
            caption (str | Unset):
            sort_order (int | Unset):
     """

    photo_id: str
    caption: str | Unset = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        photo_id = self.photo_id

        caption = self.caption

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "photo_id": photo_id,
        })
        if caption is not UNSET:
            field_dict["caption"] = caption
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_id = d.pop("photo_id")

        caption = d.pop("caption", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        update_vrbo_listing_photo_body = cls(
            photo_id=photo_id,
            caption=caption,
            sort_order=sort_order,
        )

        return update_vrbo_listing_photo_body

