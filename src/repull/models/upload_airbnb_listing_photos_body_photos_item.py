from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.upload_airbnb_listing_photos_body_photos_item_category import UploadAirbnbListingPhotosBodyPhotosItemCategory
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.upload_airbnb_listing_photos_body_photos_item_metadata import UploadAirbnbListingPhotosBodyPhotosItemMetadata





T = TypeVar("T", bound="UploadAirbnbListingPhotosBodyPhotosItem")



@_attrs_define
class UploadAirbnbListingPhotosBodyPhotosItem:
    """ 
        Attributes:
            image (str): Base64 image data. A `data:image/jpeg;base64,` prefix is accepted and stripped. Maximum 25 MB
                decoded.
            listing_id (int | str | Unset): Accepted and ignored — the listing comes from the path.
            room_id (str | Unset): Airbnb room id to file this photo under (`roomId` from `GET /rooms`).
            category (UploadAirbnbListingPhotosBodyPhotosItemCategory | Unset):
            amenity (str | Unset): Amenity id, when `category` is `listing_amenity` or `room_amenity`.
            caption (str | Unset):
            sort_order (int | Unset):
            metadata (UploadAirbnbListingPhotosBodyPhotosItemMetadata | Unset): At most 10 pairs; keys 40 characters or
                fewer.
     """

    image: str
    listing_id: int | str | Unset = UNSET
    room_id: str | Unset = UNSET
    category: UploadAirbnbListingPhotosBodyPhotosItemCategory | Unset = UNSET
    amenity: str | Unset = UNSET
    caption: str | Unset = UNSET
    sort_order: int | Unset = UNSET
    metadata: UploadAirbnbListingPhotosBodyPhotosItemMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_airbnb_listing_photos_body_photos_item_metadata import UploadAirbnbListingPhotosBodyPhotosItemMetadata
        image = self.image

        listing_id: int | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        room_id = self.room_id

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        amenity = self.amenity

        caption = self.caption

        sort_order = self.sort_order

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "image": image,
        })
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if category is not UNSET:
            field_dict["category"] = category
        if amenity is not UNSET:
            field_dict["amenity"] = amenity
        if caption is not UNSET:
            field_dict["caption"] = caption
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_airbnb_listing_photos_body_photos_item_metadata import UploadAirbnbListingPhotosBodyPhotosItemMetadata
        d = dict(src_dict)
        image = d.pop("image")

        def _parse_listing_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listing_id", UNSET))


        room_id = d.pop("room_id", UNSET)

        _category = d.pop("category", UNSET)
        category: UploadAirbnbListingPhotosBodyPhotosItemCategory | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = UploadAirbnbListingPhotosBodyPhotosItemCategory(_category)




        amenity = d.pop("amenity", UNSET)

        caption = d.pop("caption", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UploadAirbnbListingPhotosBodyPhotosItemMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = UploadAirbnbListingPhotosBodyPhotosItemMetadata.from_dict(_metadata)




        upload_airbnb_listing_photos_body_photos_item = cls(
            image=image,
            listing_id=listing_id,
            room_id=room_id,
            category=category,
            amenity=amenity,
            caption=caption,
            sort_order=sort_order,
            metadata=metadata,
        )

        return upload_airbnb_listing_photos_body_photos_item

