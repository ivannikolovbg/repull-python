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





T = TypeVar("T", bound="ListingPublishStatusResponse")



@_attrs_define
class ListingPublishStatusResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            channels (list[ListingPublishStatusChannel] | Unset): Sync activity per channel — empty if the listing has never
                been pushed/pulled. Empty does NOT mean "not connected"; check `connections` for that.
            connections (list[ListingPublishStatusConnection] | Unset): Connection state per channel. Populated even when
                `channels` is empty so callers can distinguish "owned, never pushed" from "owned, never connected".
     """

    listing_id: str | Unset = UNSET
    channels: list[ListingPublishStatusChannel] | Unset = UNSET
    connections: list[ListingPublishStatusConnection] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_publish_status_channel import ListingPublishStatusChannel
        from ..models.listing_publish_status_connection import ListingPublishStatusConnection
        listing_id = self.listing_id

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
        if channels is not UNSET:
            field_dict["channels"] = channels
        if connections is not UNSET:
            field_dict["connections"] = connections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_publish_status_channel import ListingPublishStatusChannel
        from ..models.listing_publish_status_connection import ListingPublishStatusConnection
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

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
