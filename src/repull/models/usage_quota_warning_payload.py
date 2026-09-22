from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.usage_quota_warning_payload_scope import UsageQuotaWarningPayloadScope
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.usage_quota_warning_payload_top_operation_type_0 import UsageQuotaWarningPayloadTopOperationType0





T = TypeVar("T", bound="UsageQuotaWarningPayload")



@_attrs_define
class UsageQuotaWarningPayload:
    """ Payload for `usage.quota.warning`. Sent once per account per window when usage crosses 80% of a request quota — a
    heads-up, not a refusal. `topOperation` names the operation driving the traffic so a runaway loop can be found
    before the cap stops it.

        Attributes:
            scope (UsageQuotaWarningPayloadScope | Unset): Which quota this warning is about. Example: daily_requests.
            window_key (str | Unset): The window the warning covers — the UTC date when scope is "daily_requests". Stable
                dedupe key. Example: 2026-05-01.
            tier (str | Unset):  Example: starter.
            used (int | Unset):  Example: 20000.
            limit (int | Unset):  Example: 25000.
            percent_used (int | Unset):  Example: 80.
            remaining (int | Unset):  Example: 5000.
            resets_at (datetime.datetime | Unset): When the window resets and the counter returns to zero. Example:
                2026-05-02T00:00:00.000Z.
            top_operation (None | Unset | UsageQuotaWarningPayloadTopOperationType0): The operation responsible for the
                largest share of the window so far. Absent when it could not be determined.
     """

    scope: UsageQuotaWarningPayloadScope | Unset = UNSET
    window_key: str | Unset = UNSET
    tier: str | Unset = UNSET
    used: int | Unset = UNSET
    limit: int | Unset = UNSET
    percent_used: int | Unset = UNSET
    remaining: int | Unset = UNSET
    resets_at: datetime.datetime | Unset = UNSET
    top_operation: None | Unset | UsageQuotaWarningPayloadTopOperationType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_quota_warning_payload_top_operation_type_0 import UsageQuotaWarningPayloadTopOperationType0
        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value


        window_key = self.window_key

        tier = self.tier

        used = self.used

        limit = self.limit

        percent_used = self.percent_used

        remaining = self.remaining

        resets_at: str | Unset = UNSET
        if not isinstance(self.resets_at, Unset):
            resets_at = self.resets_at.isoformat()

        top_operation: dict[str, Any] | None | Unset
        if isinstance(self.top_operation, Unset):
            top_operation = UNSET
        elif isinstance(self.top_operation, UsageQuotaWarningPayloadTopOperationType0):
            top_operation = self.top_operation.to_dict()
        else:
            top_operation = self.top_operation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if scope is not UNSET:
            field_dict["scope"] = scope
        if window_key is not UNSET:
            field_dict["windowKey"] = window_key
        if tier is not UNSET:
            field_dict["tier"] = tier
        if used is not UNSET:
            field_dict["used"] = used
        if limit is not UNSET:
            field_dict["limit"] = limit
        if percent_used is not UNSET:
            field_dict["percentUsed"] = percent_used
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if resets_at is not UNSET:
            field_dict["resetsAt"] = resets_at
        if top_operation is not UNSET:
            field_dict["topOperation"] = top_operation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_quota_warning_payload_top_operation_type_0 import UsageQuotaWarningPayloadTopOperationType0
        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: UsageQuotaWarningPayloadScope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = UsageQuotaWarningPayloadScope(_scope)




        window_key = d.pop("windowKey", UNSET)

        tier = d.pop("tier", UNSET)

        used = d.pop("used", UNSET)

        limit = d.pop("limit", UNSET)

        percent_used = d.pop("percentUsed", UNSET)

        remaining = d.pop("remaining", UNSET)

        _resets_at = d.pop("resetsAt", UNSET)
        resets_at: datetime.datetime | Unset
        if isinstance(_resets_at,  Unset):
            resets_at = UNSET
        else:
            resets_at = isoparse(_resets_at)




        def _parse_top_operation(data: object) -> None | Unset | UsageQuotaWarningPayloadTopOperationType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                top_operation_type_0 = UsageQuotaWarningPayloadTopOperationType0.from_dict(data)



                return top_operation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UsageQuotaWarningPayloadTopOperationType0, data)

        top_operation = _parse_top_operation(d.pop("topOperation", UNSET))


        usage_quota_warning_payload = cls(
            scope=scope,
            window_key=window_key,
            tier=tier,
            used=used,
            limit=limit,
            percent_used=percent_used,
            remaining=remaining,
            resets_at=resets_at,
            top_operation=top_operation,
        )


        usage_quota_warning_payload.additional_properties = d
        return usage_quota_warning_payload

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
