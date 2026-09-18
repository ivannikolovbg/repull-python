from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingPullAirbnbRequest")



@_attrs_define
class ListingPullAirbnbRequest:
    """ Optional. Omit the body entirely to pull through the listing's primary Airbnb connection.

        Attributes:
            airbnb_connection_id (str | Unset): Pull through this specific Airbnb connection instead of the listing's
                primary one. Use when a listing carries several connections (merged properties, host migrations) — the ids come
                from `GET /v1/listings/{id}/publish-status`.
     """

    airbnb_connection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        airbnb_connection_id = self.airbnb_connection_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if airbnb_connection_id is not UNSET:
            field_dict["airbnbConnectionId"] = airbnb_connection_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        airbnb_connection_id = d.pop("airbnbConnectionId", UNSET)

        listing_pull_airbnb_request = cls(
            airbnb_connection_id=airbnb_connection_id,
        )


        listing_pull_airbnb_request.additional_properties = d
        return listing_pull_airbnb_request

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
