from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_publish_status_channel import ListingPublishStatusChannel
  from ..models.listing_publish_status_connection import ListingPublishStatusConnection
  from ..models.listing_publish_status_response_address_readiness import ListingPublishStatusResponseAddressReadiness





T = TypeVar("T", bound="ListingPublishStatusResponse")



@_attrs_define
class ListingPublishStatusResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            address_readiness (ListingPublishStatusResponseAddressReadiness | Unset): Address readiness per channel, keyed
                by channel name (`airbnb` today). Airbnb requires `street` and `city` for every country and additionally `state`
                and `postalCode` for a **US** property — and a listing with no `countryCode` behaves as US. Check this BEFORE
                calling a publish endpoint: an incomplete address is refused at the create preflight and never reaches the
                channel.

                It sits here rather than inside `channels[]` because `channels` reports sync activity and is empty for a listing
                that has never been pushed — exactly the listing whose address blocker you need to see. Repair a gap with `PUT
                /v1/listings/{id}/content`, sending only the missing parts under `address`. An empty object means readiness was
                not reported; it never means ready. Example: {'airbnb': {'ready': False, 'missing': ['state', 'postalCode']}}.
            channels (list[ListingPublishStatusChannel] | Unset): Sync activity per channel — empty if the listing has never
                been pushed/pulled. Empty does NOT mean "not connected"; check `connections` for that.
            connections (list[ListingPublishStatusConnection] | Unset): Connection state per channel. Populated even when
                `channels` is empty so callers can distinguish "owned, never pushed" from "owned, never connected".
     """

    listing_id: str | Unset = UNSET
    address_readiness: ListingPublishStatusResponseAddressReadiness | Unset = UNSET
    channels: list[ListingPublishStatusChannel] | Unset = UNSET
    connections: list[ListingPublishStatusConnection] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_publish_status_channel import ListingPublishStatusChannel
        from ..models.listing_publish_status_connection import ListingPublishStatusConnection
        from ..models.listing_publish_status_response_address_readiness import ListingPublishStatusResponseAddressReadiness
        listing_id = self.listing_id

        address_readiness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address_readiness, Unset):
            address_readiness = self.address_readiness.to_dict()

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)



        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if address_readiness is not UNSET:
            field_dict["addressReadiness"] = address_readiness
        if channels is not UNSET:
            field_dict["channels"] = channels
        if connections is not UNSET:
            field_dict["connections"] = connections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_publish_status_channel import ListingPublishStatusChannel
        from ..models.listing_publish_status_connection import ListingPublishStatusConnection
        from ..models.listing_publish_status_response_address_readiness import ListingPublishStatusResponseAddressReadiness
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _address_readiness = d.pop("addressReadiness", UNSET)
        address_readiness: ListingPublishStatusResponseAddressReadiness | Unset
        if isinstance(_address_readiness,  Unset):
            address_readiness = UNSET
        else:
            address_readiness = ListingPublishStatusResponseAddressReadiness.from_dict(_address_readiness)




        _channels = d.pop("channels", UNSET)
        channels: list[ListingPublishStatusChannel] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ListingPublishStatusChannel.from_dict(channels_item_data)



                channels.append(channels_item)


        _connections = d.pop("connections", UNSET)
        connections: list[ListingPublishStatusConnection] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = ListingPublishStatusConnection.from_dict(connections_item_data)



                connections.append(connections_item)


        listing_publish_status_response = cls(
            listing_id=listing_id,
            address_readiness=address_readiness,
            channels=channels,
            connections=connections,
        )


        listing_publish_status_response.additional_properties = d
        return listing_publish_status_response

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
