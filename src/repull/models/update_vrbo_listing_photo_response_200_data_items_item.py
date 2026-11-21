from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingPhotoResponse200DataItemsItem")



@_attrs_define
class UpdateVrboListingPhotoResponse200DataItemsItem:
    """ 
        Attributes:
            id (str | Unset):
            url (None | str | Unset):
            caption (None | str | Unset):
            tags (Any | Unset): Vrbo's own tags for the photo (read-only).
            rank (int | None | Unset):
            room_ids (list[str] | Unset):
            status (None | str | Unset):
     """

    id: str | Unset = UNSET
    url: None | str | Unset = UNSET
    caption: None | str | Unset = UNSET
    tags: Any | Unset = UNSET
    rank: int | None | Unset = UNSET
    room_ids: list[str] | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        tags = self.tags

        rank: int | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        room_ids: list[str] | Unset = UNSET
        if not isinstance(self.room_ids, Unset):
            room_ids = self.room_ids



        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if caption is not UNSET:
            field_dict["caption"] = caption
        if tags is not UNSET:
            field_dict["tags"] = tags
        if rank is not UNSET:
            field_dict["rank"] = rank
        if room_ids is not UNSET:
            field_dict["roomIds"] = room_ids
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))


        tags = d.pop("tags", UNSET)

        def _parse_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))


        room_ids = cast(list[str], d.pop("roomIds", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        update_vrbo_listing_photo_response_200_data_items_item = cls(
            id=id,
            url=url,
            caption=caption,
            tags=tags,
            rank=rank,
            room_ids=room_ids,
            status=status,
        )


        update_vrbo_listing_photo_response_200_data_items_item.additional_properties = d
        return update_vrbo_listing_photo_response_200_data_items_item

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
