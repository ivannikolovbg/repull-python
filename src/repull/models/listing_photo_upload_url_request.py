from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ListingPhotoUploadUrlRequest")



@_attrs_define
class ListingPhotoUploadUrlRequest:
    """ 
        Attributes:
            file_name (str): Original file name, e.g. "living-room.jpg". Example: living-room.jpg.
            file_type (str): Image MIME type. Must start with "image/". Example: image/jpeg.
            file_size (int): File size in bytes. Required: the signed upload is issued for this size. Example: 453631.
     """

    file_name: str
    file_type: str
    file_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        file_type = self.file_type

        file_size = self.file_size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fileName": file_name,
            "fileType": file_type,
            "fileSize": file_size,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        file_type = d.pop("fileType")

        file_size = d.pop("fileSize")

        listing_photo_upload_url_request = cls(
            file_name=file_name,
            file_type=file_type,
            file_size=file_size,
        )


        listing_photo_upload_url_request.additional_properties = d
        return listing_photo_upload_url_request

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
