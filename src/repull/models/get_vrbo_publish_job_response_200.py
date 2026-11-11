from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_publish_job_response_200_channel import GetVrboPublishJobResponse200Channel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_publish_job_response_200_job import GetVrboPublishJobResponse200Job





T = TypeVar("T", bound="GetVrboPublishJobResponse200")



@_attrs_define
class GetVrboPublishJobResponse200:
    """ 
        Attributes:
            listing_id (int | Unset):
            channel (GetVrboPublishJobResponse200Channel | Unset):
            job (GetVrboPublishJobResponse200Job | Unset):
     """

    listing_id: int | Unset = UNSET
    channel: GetVrboPublishJobResponse200Channel | Unset = UNSET
    job: GetVrboPublishJobResponse200Job | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_publish_job_response_200_job import GetVrboPublishJobResponse200Job
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
        from ..models.get_vrbo_publish_job_response_200_job import GetVrboPublishJobResponse200Job
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: GetVrboPublishJobResponse200Channel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = GetVrboPublishJobResponse200Channel(_channel)




        _job = d.pop("job", UNSET)
        job: GetVrboPublishJobResponse200Job | Unset
        if isinstance(_job,  Unset):
            job = UNSET
        else:
            job = GetVrboPublishJobResponse200Job.from_dict(_job)




        get_vrbo_publish_job_response_200 = cls(
            listing_id=listing_id,
            channel=channel,
            job=job,
        )


        get_vrbo_publish_job_response_200.additional_properties = d
        return get_vrbo_publish_job_response_200

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
