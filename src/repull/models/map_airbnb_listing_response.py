from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MapAirbnbListingResponse")



@_attrs_define
class MapAirbnbListingResponse:
    """ Id fields are strings (API-wide convention — bigint ids are stringified to avoid 53-bit JS-number precision loss).

        Attributes:
            success (bool):  Example: True.
            already_mapped (bool): True when the Airbnb listing was already mapped to this listing (no-op).
            airbnb_id (str):
            listing_id (str):
            host_id (str):
            listing_airbnb_id (str): Internal id of the `listings_airbnb` record.
            platform_link_id (str): Internal id of the resulting `listing_platform_links` row.
            previous_listing_id (str | Unset): The listing the Airbnb record pointed at before this call. Omitted on a no-
                op.
     """

    success: bool
    already_mapped: bool
    airbnb_id: str
    listing_id: str
    host_id: str
    listing_airbnb_id: str
    platform_link_id: str
    previous_listing_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        already_mapped = self.already_mapped

        airbnb_id = self.airbnb_id

        listing_id = self.listing_id

        host_id = self.host_id

        listing_airbnb_id = self.listing_airbnb_id

        platform_link_id = self.platform_link_id

        previous_listing_id = self.previous_listing_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "alreadyMapped": already_mapped,
            "airbnbId": airbnb_id,
            "listingId": listing_id,
            "hostId": host_id,
            "listingAirbnbId": listing_airbnb_id,
            "platformLinkId": platform_link_id,
        })
        if previous_listing_id is not UNSET:
            field_dict["previousListingId"] = previous_listing_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        already_mapped = d.pop("alreadyMapped")

        airbnb_id = d.pop("airbnbId")

        listing_id = d.pop("listingId")

        host_id = d.pop("hostId")

        listing_airbnb_id = d.pop("listingAirbnbId")

        platform_link_id = d.pop("platformLinkId")

        previous_listing_id = d.pop("previousListingId", UNSET)

        map_airbnb_listing_response = cls(
            success=success,
            already_mapped=already_mapped,
            airbnb_id=airbnb_id,
            listing_id=listing_id,
            host_id=host_id,
            listing_airbnb_id=listing_airbnb_id,
            platform_link_id=platform_link_id,
            previous_listing_id=previous_listing_id,
        )


        map_airbnb_listing_response.additional_properties = d
        return map_airbnb_listing_response

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
