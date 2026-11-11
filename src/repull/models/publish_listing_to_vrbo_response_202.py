from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.publish_listing_to_vrbo_response_202_channel import PublishListingToVrboResponse202Channel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.publish_listing_to_vrbo_response_202_job import PublishListingToVrboResponse202Job





T = TypeVar("T", bound="PublishListingToVrboResponse202")



@_attrs_define
class PublishListingToVrboResponse202:
    """ 
        Attributes:
            listing_id (int | Unset):
            channel (PublishListingToVrboResponse202Channel | Unset):
            job (PublishListingToVrboResponse202Job | Unset):
     """

    listing_id: int | Unset = UNSET
    channel: PublishListingToVrboResponse202Channel | Unset = UNSET
    job: PublishListingToVrboResponse202Job | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_listing_to_vrbo_response_202_job import PublishListingToVrboResponse202Job
        listing_id = self.listing_id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_listing_to_vrbo_response_202_job import PublishListingToVrboResponse202Job
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: PublishListingToVrboResponse202Channel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = PublishListingToVrboResponse202Channel(_channel)




        _job = d.pop("job", UNSET)
        job: PublishListingToVrboResponse202Job | Unset
        if isinstance(_job,  Unset):
            job = UNSET
        else:
            job = PublishListingToVrboResponse202Job.from_dict(_job)




        publish_listing_to_vrbo_response_202 = cls(
            listing_id=listing_id,
            channel=channel,
            job=job,
        )


        publish_listing_to_vrbo_response_202.additional_properties = d
        return publish_listing_to_vrbo_response_202

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
