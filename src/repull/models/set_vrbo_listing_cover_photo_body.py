from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SetVrboListingCoverPhotoBody")



@_attrs_define
class SetVrboListingCoverPhotoBody:
    """ 
        Attributes:
            photo_id (str):
     """

    photo_id: str





    def to_dict(self) -> dict[str, Any]:
        photo_id = self.photo_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "photo_id": photo_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_id = d.pop("photo_id")

        set_vrbo_listing_cover_photo_body = cls(
            photo_id=photo_id,
        )

        return set_vrbo_listing_cover_photo_body

