from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_market_state_response_state import ListingMarketStateResponseState
from typing import cast

if TYPE_CHECKING:
  from ..models.channel_market_state_item import ChannelMarketStateItem





T = TypeVar("T", bound="ListingMarketStateResponse")



@_attrs_define
class ListingMarketStateResponse:
    """ The per-item result of a fan-out. **There is deliberately no top-level success flag**: a listing can sit on two
    Airbnb connections and a Booking.com property, they fail independently, and partial success is the ordinary outcome
    — any single boolean would be wrong for exactly the calls that need reading. Walk `channels` and check each `ok`.

    Nothing here is rolled back. What landed stays landed; re-send the same request to retry the items that did not,
    which is safe.

        Attributes:
            listing_id (str):
            state (ListingMarketStateResponseState): The state you asked for. Compare each item's own `state` against it.
            channels (list[ChannelMarketStateItem]): One entry per channel item acted on — Airbnb connections first, then
                the Booking.com property. Never empty: a listing connected to nothing is refused with `422
                no_connected_channels` rather than answered with an empty array.
     """

    listing_id: str
    state: ListingMarketStateResponseState
    channels: list[ChannelMarketStateItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_market_state_item import ChannelMarketStateItem
        listing_id = self.listing_id

        state = self.state.value

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "state": state,
            "channels": channels,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_market_state_item import ChannelMarketStateItem
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        state = ListingMarketStateResponseState(d.pop("state"))




        channels = []
        _channels = d.pop("channels")
        for channels_item_data in (_channels):
            channels_item = ChannelMarketStateItem.from_dict(channels_item_data)



            channels.append(channels_item)


        listing_market_state_response = cls(
            listing_id=listing_id,
            state=state,
            channels=channels,
        )


        listing_market_state_response.additional_properties = d
        return listing_market_state_response

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
