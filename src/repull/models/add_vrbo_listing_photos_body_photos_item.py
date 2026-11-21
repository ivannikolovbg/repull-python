from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AddVrboListingPhotosBodyPhotosItem")



@_attrs_define
class AddVrboListingPhotosBodyPhotosItem:
    """ 
        Attributes:
            url (str | Unset): An https JPEG or PNG Vrbo can download.
            image (str | Unset): Or: the image as base64 (a `data:image/jpeg;base64,` prefix is accepted).
            caption (str | Unset):
     """

    url: str | Unset = UNSET
    image: str | Unset = UNSET
    caption: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        image = self.image

        caption = self.caption


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if image is not UNSET:
            field_dict["image"] = image
        if caption is not UNSET:
            field_dict["caption"] = caption

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        image = d.pop("image", UNSET)

        caption = d.pop("caption", UNSET)

        add_vrbo_listing_photos_body_photos_item = cls(
            url=url,
            image=image,
            caption=caption,
        )

        return add_vrbo_listing_photos_body_photos_item

