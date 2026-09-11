from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingPhotoUploadUrlResponse")



@_attrs_define
class ListingPhotoUploadUrlResponse:
    """ A short-lived signed upload target. PUT the raw file bytes to `uploadUrl` — the bytes never pass through the Repull
    API.

        Attributes:
            listing_id (str | Unset):
            upload_url (str | Unset): PUT the raw file bytes here directly from the client. Not a Repull or vanio API
                endpoint — a signed storage URL.
            token (str | Unset): Opaque upload token bound to this signed URL.
            path (str | Unset): Storage path the photo will live at once uploaded. Pass this to `DELETE
                /v1/listings/{id}/photos` to remove it later.
            public_url (str | Unset): Durable public URL for the photo once the upload completes. Attach it to the listing
                via `PUT /v1/listings/{id}/content` (`photos` field).
            expires_in (int | Unset): Seconds until `uploadUrl` expires. Mint a new one via a fresh POST if the upload did
                not happen in time.
     """

    listing_id: str | Unset = UNSET
    upload_url: str | Unset = UNSET
    token: str | Unset = UNSET
    path: str | Unset = UNSET
    public_url: str | Unset = UNSET
    expires_in: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        upload_url = self.upload_url

        token = self.token

        path = self.path

        public_url = self.public_url

        expires_in = self.expires_in


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if upload_url is not UNSET:
            field_dict["uploadUrl"] = upload_url
        if token is not UNSET:
            field_dict["token"] = token
        if path is not UNSET:
            field_dict["path"] = path
        if public_url is not UNSET:
            field_dict["publicUrl"] = public_url
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        upload_url = d.pop("uploadUrl", UNSET)

        token = d.pop("token", UNSET)

        path = d.pop("path", UNSET)

        public_url = d.pop("publicUrl", UNSET)

        expires_in = d.pop("expiresIn", UNSET)

        listing_photo_upload_url_response = cls(
            listing_id=listing_id,
            upload_url=upload_url,
            token=token,
            path=path,
            public_url=public_url,
            expires_in=expires_in,
        )


        listing_photo_upload_url_response.additional_properties = d
        return listing_photo_upload_url_response

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
