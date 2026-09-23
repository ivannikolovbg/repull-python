from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_publish_airbnb_response_channel import ListingPublishAirbnbResponseChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_publish_result import AirbnbPublishResult





T = TypeVar("T", bound="ListingPublishAirbnbResponse")



@_attrs_define
class ListingPublishAirbnbResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            channel (ListingPublishAirbnbResponseChannel | Unset):
            result (AirbnbPublishResult | Unset): A publish is not one call to Airbnb: it is up to eight independent ones
                (details, description, amenities, rooms, policies, photos, pricing, checkout_tasks), each of which can fail on
                its own. A PARTIAL publish is normal — what succeeded stays applied; there is no rollback.

                **Content landing and the listing being live are two different answers.** `published` is about content; `live`
                is about whether the listing takes bookings. Read both.
     """

    listing_id: str | Unset = UNSET
    channel: ListingPublishAirbnbResponseChannel | Unset = UNSET
    result: AirbnbPublishResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_publish_result import AirbnbPublishResult
        listing_id = self.listing_id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_publish_result import AirbnbPublishResult
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: ListingPublishAirbnbResponseChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = ListingPublishAirbnbResponseChannel(_channel)




        _result = d.pop("result", UNSET)
        result: AirbnbPublishResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = AirbnbPublishResult.from_dict(_result)




        listing_publish_airbnb_response = cls(
            listing_id=listing_id,
            channel=channel,
            result=result,
        )


        listing_publish_airbnb_response.additional_properties = d
        return listing_publish_airbnb_response

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
