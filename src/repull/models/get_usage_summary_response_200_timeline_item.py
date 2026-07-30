from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUsageSummaryResponse200TimelineItem")



@_attrs_define
class GetUsageSummaryResponse200TimelineItem:
    """ 
        Attributes:
            day (str | Unset):
            request_count (int | Unset):
            error_count (int | Unset):
     """

    day: str | Unset = UNSET
    request_count: int | Unset = UNSET
    error_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        day = self.day

        request_count = self.request_count

        error_count = self.error_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if day is not UNSET:
            field_dict["day"] = day
        if request_count is not UNSET:
            field_dict["requestCount"] = request_count
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day", UNSET)

        request_count = d.pop("requestCount", UNSET)

        error_count = d.pop("errorCount", UNSET)

        get_usage_summary_response_200_timeline_item = cls(
            day=day,
            request_count=request_count,
            error_count=error_count,
        )


        get_usage_summary_response_200_timeline_item.additional_properties = d
        return get_usage_summary_response_200_timeline_item

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
