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
  from ..models.get_usage_summary_response_200_breakdown_item import GetUsageSummaryResponse200BreakdownItem
  from ..models.get_usage_summary_response_200_limits import GetUsageSummaryResponse200Limits
  from ..models.get_usage_summary_response_200_remaining import GetUsageSummaryResponse200Remaining
  from ..models.get_usage_summary_response_200_status_distribution import GetUsageSummaryResponse200StatusDistribution
  from ..models.get_usage_summary_response_200_timeline_item import GetUsageSummaryResponse200TimelineItem
  from ..models.get_usage_summary_response_200_totals import GetUsageSummaryResponse200Totals
  from ..models.get_usage_summary_response_200_used import GetUsageSummaryResponse200Used





T = TypeVar("T", bound="GetUsageSummaryResponse200")



@_attrs_define
class GetUsageSummaryResponse200:
    """ 
        Attributes:
            tier (str | Unset):
            limits (GetUsageSummaryResponse200Limits | Unset):
            used (GetUsageSummaryResponse200Used | Unset):
            remaining (GetUsageSummaryResponse200Remaining | Unset):
            resets_at (datetime.datetime | Unset):
            breakdown (list[GetUsageSummaryResponse200BreakdownItem] | Unset):
            timeline (list[GetUsageSummaryResponse200TimelineItem] | Unset):
            status_distribution (GetUsageSummaryResponse200StatusDistribution | Unset):
            totals (GetUsageSummaryResponse200Totals | Unset):
            range_ (str | Unset):
     """

    tier: str | Unset = UNSET
    limits: GetUsageSummaryResponse200Limits | Unset = UNSET
    used: GetUsageSummaryResponse200Used | Unset = UNSET
    remaining: GetUsageSummaryResponse200Remaining | Unset = UNSET
    resets_at: datetime.datetime | Unset = UNSET
    breakdown: list[GetUsageSummaryResponse200BreakdownItem] | Unset = UNSET
    timeline: list[GetUsageSummaryResponse200TimelineItem] | Unset = UNSET
    status_distribution: GetUsageSummaryResponse200StatusDistribution | Unset = UNSET
    totals: GetUsageSummaryResponse200Totals | Unset = UNSET
    range_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_usage_summary_response_200_breakdown_item import GetUsageSummaryResponse200BreakdownItem
        from ..models.get_usage_summary_response_200_limits import GetUsageSummaryResponse200Limits
        from ..models.get_usage_summary_response_200_remaining import GetUsageSummaryResponse200Remaining
        from ..models.get_usage_summary_response_200_status_distribution import GetUsageSummaryResponse200StatusDistribution
        from ..models.get_usage_summary_response_200_timeline_item import GetUsageSummaryResponse200TimelineItem
        from ..models.get_usage_summary_response_200_totals import GetUsageSummaryResponse200Totals
        from ..models.get_usage_summary_response_200_used import GetUsageSummaryResponse200Used
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

        breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = []
            for breakdown_item_data in self.breakdown:
                breakdown_item = breakdown_item_data.to_dict()
                breakdown.append(breakdown_item)



        timeline: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timeline, Unset):
            timeline = []
            for timeline_item_data in self.timeline:
                timeline_item = timeline_item_data.to_dict()
                timeline.append(timeline_item)



        status_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_distribution, Unset):
            status_distribution = self.status_distribution.to_dict()

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        range_ = self.range_


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
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if timeline is not UNSET:
            field_dict["timeline"] = timeline
        if status_distribution is not UNSET:
            field_dict["statusDistribution"] = status_distribution
        if totals is not UNSET:
            field_dict["totals"] = totals
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_usage_summary_response_200_breakdown_item import GetUsageSummaryResponse200BreakdownItem
        from ..models.get_usage_summary_response_200_limits import GetUsageSummaryResponse200Limits
        from ..models.get_usage_summary_response_200_remaining import GetUsageSummaryResponse200Remaining
        from ..models.get_usage_summary_response_200_status_distribution import GetUsageSummaryResponse200StatusDistribution
        from ..models.get_usage_summary_response_200_timeline_item import GetUsageSummaryResponse200TimelineItem
        from ..models.get_usage_summary_response_200_totals import GetUsageSummaryResponse200Totals
        from ..models.get_usage_summary_response_200_used import GetUsageSummaryResponse200Used
        d = dict(src_dict)
        tier = d.pop("tier", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: GetUsageSummaryResponse200Limits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = GetUsageSummaryResponse200Limits.from_dict(_limits)




        _used = d.pop("used", UNSET)
        used: GetUsageSummaryResponse200Used | Unset
        if isinstance(_used,  Unset):
            used = UNSET
        else:
            used = GetUsageSummaryResponse200Used.from_dict(_used)




        _remaining = d.pop("remaining", UNSET)
        remaining: GetUsageSummaryResponse200Remaining | Unset
        if isinstance(_remaining,  Unset):
            remaining = UNSET
        else:
            remaining = GetUsageSummaryResponse200Remaining.from_dict(_remaining)




        _resets_at = d.pop("resets_at", UNSET)
        resets_at: datetime.datetime | Unset
        if isinstance(_resets_at,  Unset):
            resets_at = UNSET
        else:
            resets_at = isoparse(_resets_at)




        _breakdown = d.pop("breakdown", UNSET)
        breakdown: list[GetUsageSummaryResponse200BreakdownItem] | Unset = UNSET
        if _breakdown is not UNSET:
            breakdown = []
            for breakdown_item_data in _breakdown:
                breakdown_item = GetUsageSummaryResponse200BreakdownItem.from_dict(breakdown_item_data)



                breakdown.append(breakdown_item)


        _timeline = d.pop("timeline", UNSET)
        timeline: list[GetUsageSummaryResponse200TimelineItem] | Unset = UNSET
        if _timeline is not UNSET:
            timeline = []
            for timeline_item_data in _timeline:
                timeline_item = GetUsageSummaryResponse200TimelineItem.from_dict(timeline_item_data)



                timeline.append(timeline_item)


        _status_distribution = d.pop("statusDistribution", UNSET)
        status_distribution: GetUsageSummaryResponse200StatusDistribution | Unset
        if isinstance(_status_distribution,  Unset):
            status_distribution = UNSET
        else:
            status_distribution = GetUsageSummaryResponse200StatusDistribution.from_dict(_status_distribution)




        _totals = d.pop("totals", UNSET)
        totals: GetUsageSummaryResponse200Totals | Unset
        if isinstance(_totals,  Unset):
            totals = UNSET
        else:
            totals = GetUsageSummaryResponse200Totals.from_dict(_totals)




        range_ = d.pop("range", UNSET)

        get_usage_summary_response_200 = cls(
            tier=tier,
            limits=limits,
            used=used,
            remaining=remaining,
            resets_at=resets_at,
            breakdown=breakdown,
            timeline=timeline,
            status_distribution=status_distribution,
            totals=totals,
            range_=range_,
        )


        get_usage_summary_response_200.additional_properties = d
        return get_usage_summary_response_200

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
