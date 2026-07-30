from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUsageSummaryResponse200Totals")



@_attrs_define
class GetUsageSummaryResponse200Totals:
    """ 
        Attributes:
            requests (int | Unset):
            errors (int | Unset):
            avg_latency_ms (int | Unset):
     """

    requests: int | Unset = UNSET
    errors: int | Unset = UNSET
    avg_latency_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        errors = self.errors

        avg_latency_ms = self.avg_latency_ms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if requests is not UNSET:
            field_dict["requests"] = requests
        if errors is not UNSET:
            field_dict["errors"] = errors
        if avg_latency_ms is not UNSET:
            field_dict["avgLatencyMs"] = avg_latency_ms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests = d.pop("requests", UNSET)

        errors = d.pop("errors", UNSET)

        avg_latency_ms = d.pop("avgLatencyMs", UNSET)

        get_usage_summary_response_200_totals = cls(
            requests=requests,
            errors=errors,
            avg_latency_ms=avg_latency_ms,
        )


        get_usage_summary_response_200_totals.additional_properties = d
        return get_usage_summary_response_200_totals

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
