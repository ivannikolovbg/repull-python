from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.listing_address_readiness import ListingAddressReadiness





T = TypeVar("T", bound="ListingPublishStatusResponseAddressReadiness")



@_attrs_define
class ListingPublishStatusResponseAddressReadiness:
    """ Address readiness per channel, keyed by channel name (`airbnb` today). Airbnb requires `street` and `city` for every
    country and additionally `state` and `postalCode` for a **US** property — and a listing with no `countryCode`
    behaves as US. Check this BEFORE calling a publish endpoint: an incomplete address is refused at the create
    preflight and never reaches the channel.

    It sits here rather than inside `channels[]` because `channels` reports sync activity and is empty for a listing
    that has never been pushed — exactly the listing whose address blocker you need to see. Repair a gap with `PUT
    /v1/listings/{id}/content`, sending only the missing parts under `address`. An empty object means readiness was not
    reported; it never means ready.

        Example:
            {'airbnb': {'ready': False, 'missing': ['state', 'postalCode']}}

     """

    additional_properties: dict[str, ListingAddressReadiness] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_address_readiness import ListingAddressReadiness
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_address_readiness import ListingAddressReadiness
        d = dict(src_dict)
        listing_publish_status_response_address_readiness = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ListingAddressReadiness.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        listing_publish_status_response_address_readiness.additional_properties = additional_properties
        return listing_publish_status_response_address_readiness

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ListingAddressReadiness:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ListingAddressReadiness) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
