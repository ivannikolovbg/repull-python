from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingAvailabilityResponse202Data")



@_attrs_define
class UpdateVrboListingAvailabilityResponse202Data:
    """ 
        Attributes:
            job_id (str | Unset):
            status (str | Unset):  Example: queued.
            nights (int | Unset):
     """

    job_id: str | Unset = UNSET
    status: str | Unset = UNSET
    nights: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        status = self.status

        nights = self.nights


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if status is not UNSET:
            field_dict["status"] = status
        if nights is not UNSET:
            field_dict["nights"] = nights

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        status = d.pop("status", UNSET)

        nights = d.pop("nights", UNSET)

        update_vrbo_listing_availability_response_202_data = cls(
            job_id=job_id,
            status=status,
            nights=nights,
        )


        update_vrbo_listing_availability_response_202_data.additional_properties = d
        return update_vrbo_listing_availability_response_202_data

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
