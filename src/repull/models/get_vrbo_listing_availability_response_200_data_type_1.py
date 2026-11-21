from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_availability_response_200_data_type_1_stats_type_0 import GetVrboListingAvailabilityResponse200DataType1StatsType0





T = TypeVar("T", bound="GetVrboListingAvailabilityResponse200DataType1")



@_attrs_define
class GetVrboListingAvailabilityResponse200DataType1:
    """ With `jobId`: the write's job.

        Attributes:
            job_id (int | Unset):
            status (str | Unset):  Example: done.
            nights (int | Unset):
            queued_at (None | str | Unset):
            finished_at (None | str | Unset):
            error (None | str | Unset):
            stats (GetVrboListingAvailabilityResponse200DataType1StatsType0 | None | Unset):
     """

    job_id: int | Unset = UNSET
    status: str | Unset = UNSET
    nights: int | Unset = UNSET
    queued_at: None | str | Unset = UNSET
    finished_at: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    stats: GetVrboListingAvailabilityResponse200DataType1StatsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_availability_response_200_data_type_1_stats_type_0 import GetVrboListingAvailabilityResponse200DataType1StatsType0
        job_id = self.job_id

        status = self.status

        nights = self.nights

        queued_at: None | str | Unset
        if isinstance(self.queued_at, Unset):
            queued_at = UNSET
        else:
            queued_at = self.queued_at

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = self.finished_at

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, GetVrboListingAvailabilityResponse200DataType1StatsType0):
            stats = self.stats.to_dict()
        else:
            stats = self.stats


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
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if error is not UNSET:
            field_dict["error"] = error
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_availability_response_200_data_type_1_stats_type_0 import GetVrboListingAvailabilityResponse200DataType1StatsType0
        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        status = d.pop("status", UNSET)

        nights = d.pop("nights", UNSET)

        def _parse_queued_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queued_at = _parse_queued_at(d.pop("queuedAt", UNSET))


        def _parse_finished_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_stats(data: object) -> GetVrboListingAvailabilityResponse200DataType1StatsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = GetVrboListingAvailabilityResponse200DataType1StatsType0.from_dict(data)



                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingAvailabilityResponse200DataType1StatsType0 | None | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))


        get_vrbo_listing_availability_response_200_data_type_1 = cls(
            job_id=job_id,
            status=status,
            nights=nights,
            queued_at=queued_at,
            finished_at=finished_at,
            error=error,
            stats=stats,
        )


        get_vrbo_listing_availability_response_200_data_type_1.additional_properties = d
        return get_vrbo_listing_availability_response_200_data_type_1

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
