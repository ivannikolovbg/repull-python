from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_usage_tier_response_200_limits import GetUsageTierResponse200Limits
  from ..models.get_usage_tier_response_200_remaining import GetUsageTierResponse200Remaining
  from ..models.get_usage_tier_response_200_used import GetUsageTierResponse200Used





T = TypeVar("T", bound="GetUsageTierResponse200")



@_attrs_define
class GetUsageTierResponse200:
    """ 
        Attributes:
            tier (str | Unset):
            limits (GetUsageTierResponse200Limits | Unset):
            used (GetUsageTierResponse200Used | Unset):
            remaining (GetUsageTierResponse200Remaining | Unset):
            resets_at (datetime.datetime | Unset):
     """

    tier: str | Unset = UNSET
    limits: GetUsageTierResponse200Limits | Unset = UNSET
    used: GetUsageTierResponse200Used | Unset = UNSET
    remaining: GetUsageTierResponse200Remaining | Unset = UNSET
    resets_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_usage_tier_response_200_limits import GetUsageTierResponse200Limits
        from ..models.get_usage_tier_response_200_remaining import GetUsageTierResponse200Remaining
        from ..models.get_usage_tier_response_200_used import GetUsageTierResponse200Used
        tier = self.tier

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        used: dict[str, Any] | Unset = UNSET
        if not isinstance(self.used, Unset):
            used = self.used.to_dict()

        remaining: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remaining, Unset):
            remaining = self.remaining.to_dict()

        resets_at: str | Unset = UNSET
        if not isinstance(self.resets_at, Unset):
            resets_at = self.resets_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tier is not UNSET:
            field_dict["tier"] = tier
        if limits is not UNSET:
            field_dict["limits"] = limits
        if used is not UNSET:
            field_dict["used"] = used
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if resets_at is not UNSET:
            field_dict["resets_at"] = resets_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_usage_tier_response_200_limits import GetUsageTierResponse200Limits
        from ..models.get_usage_tier_response_200_remaining import GetUsageTierResponse200Remaining
        from ..models.get_usage_tier_response_200_used import GetUsageTierResponse200Used
        d = dict(src_dict)
        tier = d.pop("tier", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: GetUsageTierResponse200Limits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = GetUsageTierResponse200Limits.from_dict(_limits)




        _used = d.pop("used", UNSET)
        used: GetUsageTierResponse200Used | Unset
        if isinstance(_used,  Unset):
            used = UNSET
        else:
            used = GetUsageTierResponse200Used.from_dict(_used)




        _remaining = d.pop("remaining", UNSET)
        remaining: GetUsageTierResponse200Remaining | Unset
        if isinstance(_remaining,  Unset):
            remaining = UNSET
        else:
            remaining = GetUsageTierResponse200Remaining.from_dict(_remaining)




        _resets_at = d.pop("resets_at", UNSET)
        resets_at: datetime.datetime | Unset
        if isinstance(_resets_at,  Unset):
            resets_at = UNSET
        else:
            resets_at = isoparse(_resets_at)




        get_usage_tier_response_200 = cls(
            tier=tier,
            limits=limits,
            used=used,
            remaining=remaining,
            resets_at=resets_at,
        )


        get_usage_tier_response_200.additional_properties = d
        return get_usage_tier_response_200

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
