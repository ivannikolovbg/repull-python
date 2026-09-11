from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_photo import ListingPhoto





T = TypeVar("T", bound="ListingPhotosResponse")



@_attrs_define
class ListingPhotosResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            photos (list[ListingPhoto] | Unset):
     """

    listing_id: str | Unset = UNSET
    photos: list[ListingPhoto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_photo import ListingPhoto
        listing_id = self.listing_id

        photos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = []
            for photos_item_data in self.photos:
                photos_item = photos_item_data.to_dict()
                photos.append(photos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if photos is not UNSET:
            field_dict["photos"] = photos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_photo import ListingPhoto
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _photos = d.pop("photos", UNSET)
        photos: list[ListingPhoto] | Unset = UNSET
        if _photos is not UNSET:
            photos = []
            for photos_item_data in _photos:
                photos_item = ListingPhoto.from_dict(photos_item_data)



                photos.append(photos_item)


        listing_photos_response = cls(
            listing_id=listing_id,
            photos=photos,
        )


        listing_photos_response.additional_properties = d
        return listing_photos_response

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
