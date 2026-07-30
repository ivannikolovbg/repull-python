from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUsageSummaryResponse200BreakdownItem")



@_attrs_define
class GetUsageSummaryResponse200BreakdownItem:
    """ 
        Attributes:
            operation_id (str | Unset):
            request_count (int | Unset):
            error_count (int | Unset):
            error_rate (float | Unset):
            avg_latency_ms (int | Unset):
     """

    operation_id: str | Unset = UNSET
    request_count: int | Unset = UNSET
    error_count: int | Unset = UNSET
    error_rate: float | Unset = UNSET
    avg_latency_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        request_count = self.request_count

        error_count = self.error_count

        error_rate = self.error_rate

        avg_latency_ms = self.avg_latency_ms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if request_count is not UNSET:
            field_dict["requestCount"] = request_count
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count
        if error_rate is not UNSET:
            field_dict["errorRate"] = error_rate
        if avg_latency_ms is not UNSET:
            field_dict["avgLatencyMs"] = avg_latency_ms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operationId", UNSET)

        request_count = d.pop("requestCount", UNSET)

        error_count = d.pop("errorCount", UNSET)

        error_rate = d.pop("errorRate", UNSET)

        avg_latency_ms = d.pop("avgLatencyMs", UNSET)

        get_usage_summary_response_200_breakdown_item = cls(
            operation_id=operation_id,
            request_count=request_count,
            error_count=error_count,
            error_rate=error_rate,
            avg_latency_ms=avg_latency_ms,
        )


        get_usage_summary_response_200_breakdown_item.additional_properties = d
        return get_usage_summary_response_200_breakdown_item

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
