from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.upload_airbnb_listing_photos_body_photos_item import UploadAirbnbListingPhotosBodyPhotosItem





T = TypeVar("T", bound="UploadAirbnbListingPhotosBody")



@_attrs_define
class UploadAirbnbListingPhotosBody:
    """ 
        Attributes:
            photos (list[UploadAirbnbListingPhotosBodyPhotosItem]):
     """

    photos: list[UploadAirbnbListingPhotosBodyPhotosItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_airbnb_listing_photos_body_photos_item import UploadAirbnbListingPhotosBodyPhotosItem
        photos = []
        for photos_item_data in self.photos:
            photos_item = photos_item_data.to_dict()
            photos.append(photos_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "photos": photos,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_airbnb_listing_photos_body_photos_item import UploadAirbnbListingPhotosBodyPhotosItem
        d = dict(src_dict)
        photos = []
        _photos = d.pop("photos")
        for photos_item_data in (_photos):
            photos_item = UploadAirbnbListingPhotosBodyPhotosItem.from_dict(photos_item_data)



            photos.append(photos_item)


        upload_airbnb_listing_photos_body = cls(
            photos=photos,
        )

        return upload_airbnb_listing_photos_body

