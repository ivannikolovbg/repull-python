from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentPhoto")



@_attrs_define
class ListingContentPhoto:
    """ 
        Attributes:
            url (str | Unset):
            thumbnail_url (None | str | Unset):
            caption (None | str | Unset):
            category (None | str | Unset):
            width (int | None | Unset):
            height (int | None | Unset):
            sort_order (int | Unset):
     """

    url: str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    caption: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    sort_order: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if caption is not UNSET:
            field_dict["caption"] = caption
        if category is not UNSET:
            field_dict["category"] = category
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))


        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))


        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        listing_content_photo = cls(
            url=url,
            thumbnail_url=thumbnail_url,
            caption=caption,
            category=category,
            width=width,
            height=height,
            sort_order=sort_order,
        )


        listing_content_photo.additional_properties = d
        return listing_content_photo

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
