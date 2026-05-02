from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_publish_response_channel import ListingPublishResponseChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_publish_response_result import ListingPublishResponseResult





T = TypeVar("T", bound="ListingPublishResponse")



@_attrs_define
class ListingPublishResponse:
    """ 
        Attributes:
            listing_id (int | Unset):
            channel (ListingPublishResponseChannel | Unset):
            result (ListingPublishResponseResult | Unset): Channel-specific push result (sections pushed, errors, etc.)
     """

    listing_id: int | Unset = UNSET
    channel: ListingPublishResponseChannel | Unset = UNSET
    result: ListingPublishResponseResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_publish_response_result import ListingPublishResponseResult
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
        from ..models.listing_publish_response_result import ListingPublishResponseResult
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: ListingPublishResponseChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = ListingPublishResponseChannel(_channel)




        _result = d.pop("result", UNSET)
        result: ListingPublishResponseResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = ListingPublishResponseResult.from_dict(_result)




        listing_publish_response = cls(
            listing_id=listing_id,
            channel=channel,
            result=result,
        )


        listing_publish_response.additional_properties = d
        return listing_publish_response

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
