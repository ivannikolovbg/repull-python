from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsageQuotaWarningPayloadTopOperationType0")



@_attrs_define
class UsageQuotaWarningPayloadTopOperationType0:
    """ The operation responsible for the largest share of the window so far. Absent when it could not be determined.

        Attributes:
            operation_id (str | Unset):  Example: replay_webhook_delivery.
            request_count (int | Unset):  Example: 17000.
            share_percent (float | Unset): Share of the window's requests, 0-100. Example: 85.
     """

    operation_id: str | Unset = UNSET
    request_count: int | Unset = UNSET
    share_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        request_count = self.request_count

        share_percent = self.share_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if request_count is not UNSET:
            field_dict["requestCount"] = request_count
        if share_percent is not UNSET:
            field_dict["sharePercent"] = share_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operationId", UNSET)

        request_count = d.pop("requestCount", UNSET)

        share_percent = d.pop("sharePercent", UNSET)

        usage_quota_warning_payload_top_operation_type_0 = cls(
            operation_id=operation_id,
            request_count=request_count,
            share_percent=share_percent,
        )


        usage_quota_warning_payload_top_operation_type_0.additional_properties = d
        return usage_quota_warning_payload_top_operation_type_0

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
