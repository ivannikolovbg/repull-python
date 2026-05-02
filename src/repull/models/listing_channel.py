from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingChannel")



@_attrs_define
class ListingChannel:
    """ Per-platform connection for a listing — one row per channel the listing is published to.

        Attributes:
            platform (str | Unset):  Example: airbnb.
            external_id (str | Unset): ID in the platform (Airbnb listing id, Booking room id, etc.)
            active (bool | Unset):
            sync_enabled (bool | Unset):
     """

    platform: str | Unset = UNSET
    external_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        external_id = self.external_id

        active = self.active

        sync_enabled = self.sync_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if platform is not UNSET:
            field_dict["platform"] = platform
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if active is not UNSET:
            field_dict["active"] = active
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        external_id = d.pop("externalId", UNSET)

        active = d.pop("active", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        listing_channel = cls(
            platform=platform,
            external_id=external_id,
            active=active,
            sync_enabled=sync_enabled,
        )


        listing_channel.additional_properties = d
        return listing_channel

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
