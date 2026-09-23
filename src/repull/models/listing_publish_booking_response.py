from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_publish_booking_response_channel import ListingPublishBookingResponseChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_publish_result import BookingPublishResult





T = TypeVar("T", bound="ListingPublishBookingResponse")



@_attrs_define
class ListingPublishBookingResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            channel (ListingPublishBookingResponseChannel | Unset):
            result (BookingPublishResult | Unset): A publish is not one call to Booking.com: it is several independent
                Content API calls (details, description, amenities, rooms, photos, pricing), each of which can fail on its own.
                A PARTIAL publish is normal — what succeeded stays applied; there is no rollback. Fix the failing sections and
                publish again; re-publishing an unchanged section is harmless.

                A property whose Content API credentials do not cover a section answers 403 for that section alone — the rest
                still land, and the failure is reported here rather than swallowed.
     """

    listing_id: str | Unset = UNSET
    channel: ListingPublishBookingResponseChannel | Unset = UNSET
    result: BookingPublishResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_publish_result import BookingPublishResult
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
        from ..models.booking_publish_result import BookingPublishResult
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: ListingPublishBookingResponseChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = ListingPublishBookingResponseChannel(_channel)




        _result = d.pop("result", UNSET)
        result: BookingPublishResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = BookingPublishResult.from_dict(_result)




        listing_publish_booking_response = cls(
            listing_id=listing_id,
            channel=channel,
            result=result,
        )


        listing_publish_booking_response.additional_properties = d
        return listing_publish_booking_response

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
