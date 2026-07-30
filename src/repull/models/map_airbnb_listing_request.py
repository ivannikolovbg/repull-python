from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MapAirbnbListingRequest")



@_attrs_define
class MapAirbnbListingRequest:
    """ Body for `POST /v1/channels/airbnb/listings/map`.

        Attributes:
            airbnb_id (str): The Airbnb listing id to map. Discover it via `GET /v1/channels/airbnb/listings`.
            listing_id (int): Canonical Repull listing id to link the Airbnb listing to. Must belong to your workspace. A
                numeric string is also accepted.
            host_id (str | Unset): Optional. When present, must match the Airbnb listing's host id — guards against mapping
                the wrong host's listing.
            sync_enabled (bool | Unset): Whether the resulting platform link has sync enabled. Default: True.
     """

    airbnb_id: str
    listing_id: int
    host_id: str | Unset = UNSET
    sync_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        airbnb_id = self.airbnb_id

        listing_id = self.listing_id

        host_id = self.host_id

        sync_enabled = self.sync_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "airbnbId": airbnb_id,
            "listingId": listing_id,
        })
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        airbnb_id = d.pop("airbnbId")

        listing_id = d.pop("listingId")

        host_id = d.pop("hostId", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        map_airbnb_listing_request = cls(
            airbnb_id=airbnb_id,
            listing_id=listing_id,
            host_id=host_id,
            sync_enabled=sync_enabled,
        )


        map_airbnb_listing_request.additional_properties = d
        return map_airbnb_listing_request

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
