from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_created_payload_address import ListingCreatedPayloadAddress





T = TypeVar("T", bound="ListingCreatedPayload")



@_attrs_define
class ListingCreatedPayload:
    """ Payload for `listing.created`. A new property was synced into Repull from a connected PMS or channel.

        Attributes:
            id (int | Unset):  Example: 6250.
            title (str | Unset):  Example: R-Sable 1302 — Radium Hot Springs.
            address (ListingCreatedPayloadAddress | Unset):
            bedrooms (int | Unset):  Example: 2.
            bathrooms (float | Unset):  Example: 2.
            max_guests (int | Unset):  Example: 6.
            created_at (datetime.datetime | Unset):  Example: 2026-05-01T12:00:00.000Z.
     """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    address: ListingCreatedPayloadAddress | Unset = UNSET
    bedrooms: int | Unset = UNSET
    bathrooms: float | Unset = UNSET
    max_guests: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_created_payload_address import ListingCreatedPayloadAddress
        id = self.id

        title = self.title

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        bedrooms = self.bedrooms

        bathrooms = self.bathrooms

        max_guests = self.max_guests

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if address is not UNSET:
            field_dict["address"] = address
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_created_payload_address import ListingCreatedPayloadAddress
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _address = d.pop("address", UNSET)
        address: ListingCreatedPayloadAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = ListingCreatedPayloadAddress.from_dict(_address)




        bedrooms = d.pop("bedrooms", UNSET)

        bathrooms = d.pop("bathrooms", UNSET)

        max_guests = d.pop("maxGuests", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        listing_created_payload = cls(
            id=id,
            title=title,
            address=address,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            max_guests=max_guests,
            created_at=created_at,
        )


        listing_created_payload.additional_properties = d
        return listing_created_payload

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
