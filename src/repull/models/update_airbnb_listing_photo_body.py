from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_photo_body_metadata_type_0 import UpdateAirbnbListingPhotoBodyMetadataType0





T = TypeVar("T", bound="UpdateAirbnbListingPhotoBody")



@_attrs_define
class UpdateAirbnbListingPhotoBody:
    """ `photo_id` plus at least one of `caption`, `sort_order`, `room_id`, `metadata`.

        Attributes:
            photo_id (str): Airbnb-side photo id — the `photoAirbnbId` from `GET /photos`.
            caption (None | str | Unset): New caption, or `null` to clear it.
            sort_order (int | None | Unset): Position in the tour. Relative, not absolute — lower sorts earlier.
            room_id (None | str | Unset): Airbnb room id to file the photo under (`roomId` from `GET /rooms`), or `null` to
                detach it.
            metadata (None | Unset | UpdateAirbnbListingPhotoBodyMetadataType0): At most 10 pairs; keys 40 characters or
                fewer.
     """

    photo_id: str
    caption: None | str | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    room_id: None | str | Unset = UNSET
    metadata: None | Unset | UpdateAirbnbListingPhotoBodyMetadataType0 = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_photo_body_metadata_type_0 import UpdateAirbnbListingPhotoBodyMetadataType0
        photo_id = self.photo_id

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        room_id: None | str | Unset
        if isinstance(self.room_id, Unset):
            room_id = UNSET
        else:
            room_id = self.room_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateAirbnbListingPhotoBodyMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "photo_id": photo_id,
        })
        if caption is not UNSET:
            field_dict["caption"] = caption
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_listing_photo_body_metadata_type_0 import UpdateAirbnbListingPhotoBodyMetadataType0
        d = dict(src_dict)
        photo_id = d.pop("photo_id")

        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))


        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))


        def _parse_room_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_id = _parse_room_id(d.pop("room_id", UNSET))


        def _parse_metadata(data: object) -> None | Unset | UpdateAirbnbListingPhotoBodyMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateAirbnbListingPhotoBodyMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAirbnbListingPhotoBodyMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        update_airbnb_listing_photo_body = cls(
            photo_id=photo_id,
            caption=caption,
            sort_order=sort_order,
            room_id=room_id,
            metadata=metadata,
        )

        return update_airbnb_listing_photo_body

