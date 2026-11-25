from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_publish_tiket_response_channel import ListingPublishTiketResponseChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_publish_tiket_response_result import ListingPublishTiketResponseResult





T = TypeVar("T", bound="ListingPublishTiketResponse")



@_attrs_define
class ListingPublishTiketResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            channel (ListingPublishTiketResponseChannel | Unset):
            result (ListingPublishTiketResponseResult | Unset):
     """

    listing_id: str | Unset = UNSET
    channel: ListingPublishTiketResponseChannel | Unset = UNSET
    result: ListingPublishTiketResponseResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_publish_tiket_response_result import ListingPublishTiketResponseResult
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
        from ..models.listing_publish_tiket_response_result import ListingPublishTiketResponseResult
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: ListingPublishTiketResponseChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = ListingPublishTiketResponseChannel(_channel)




        _result = d.pop("result", UNSET)
        result: ListingPublishTiketResponseResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = ListingPublishTiketResponseResult.from_dict(_result)




        listing_publish_tiket_response = cls(
            listing_id=listing_id,
            channel=channel,
            result=result,
        )


        listing_publish_tiket_response.additional_properties = d
        return listing_publish_tiket_response

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
