from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_pricing_history_entry_status import ListingPricingHistoryEntryStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_pricing_history_entry_recommendation_factors import ListingPricingHistoryEntryRecommendationFactors





T = TypeVar("T", bound="ListingPricingHistoryEntry")



@_attrs_define
class ListingPricingHistoryEntry:
    """ One date in the recommendation-vs-applied audit trail.

        Attributes:
            date (datetime.date | Unset):
            recommended_rate (float | Unset): The Atlas model's recommended price for the date.
            applied_rate (float | None | Unset): Price actually written to the calendar. `null` when status is `pending` or
                `declined`. For now, when `status=applied` this equals `recommended_rate` because the apply path writes the
                recommendation verbatim.
            status (ListingPricingHistoryEntryStatus | Unset): `overridden` is reserved for a future signal — it never
                appears today.
            recommendation_factors (ListingPricingHistoryEntryRecommendationFactors | Unset): Raw model factors (comp
                distance, event boost, weekend, demand, etc.).
            applied_at (datetime.datetime | None | Unset):
            applied_by (None | str | Unset): Who applied it (e.g. `auto`, `api`, `user`).
     """

    date: datetime.date | Unset = UNSET
    recommended_rate: float | Unset = UNSET
    applied_rate: float | None | Unset = UNSET
    status: ListingPricingHistoryEntryStatus | Unset = UNSET
    recommendation_factors: ListingPricingHistoryEntryRecommendationFactors | Unset = UNSET
    applied_at: datetime.datetime | None | Unset = UNSET
    applied_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pricing_history_entry_recommendation_factors import ListingPricingHistoryEntryRecommendationFactors
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        recommended_rate = self.recommended_rate

        applied_rate: float | None | Unset
        if isinstance(self.applied_rate, Unset):
            applied_rate = UNSET
        else:
            applied_rate = self.applied_rate

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        recommendation_factors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommendation_factors, Unset):
            recommendation_factors = self.recommendation_factors.to_dict()

        applied_at: None | str | Unset
        if isinstance(self.applied_at, Unset):
            applied_at = UNSET
        elif isinstance(self.applied_at, datetime.datetime):
            applied_at = self.applied_at.isoformat()
        else:
            applied_at = self.applied_at

        applied_by: None | str | Unset
        if isinstance(self.applied_by, Unset):
            applied_by = UNSET
        else:
            applied_by = self.applied_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if recommended_rate is not UNSET:
            field_dict["recommendedRate"] = recommended_rate
        if applied_rate is not UNSET:
            field_dict["appliedRate"] = applied_rate
        if status is not UNSET:
            field_dict["status"] = status
        if recommendation_factors is not UNSET:
            field_dict["recommendationFactors"] = recommendation_factors
        if applied_at is not UNSET:
            field_dict["appliedAt"] = applied_at
        if applied_by is not UNSET:
            field_dict["appliedBy"] = applied_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pricing_history_entry_recommendation_factors import ListingPricingHistoryEntryRecommendationFactors
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        recommended_rate = d.pop("recommendedRate", UNSET)

        def _parse_applied_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        applied_rate = _parse_applied_rate(d.pop("appliedRate", UNSET))


        _status = d.pop("status", UNSET)
        status: ListingPricingHistoryEntryStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ListingPricingHistoryEntryStatus(_status)




        _recommendation_factors = d.pop("recommendationFactors", UNSET)
        recommendation_factors: ListingPricingHistoryEntryRecommendationFactors | Unset
        if isinstance(_recommendation_factors,  Unset):
            recommendation_factors = UNSET
        else:
            recommendation_factors = ListingPricingHistoryEntryRecommendationFactors.from_dict(_recommendation_factors)




        def _parse_applied_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_at_type_0 = isoparse(data)



                return applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        applied_at = _parse_applied_at(d.pop("appliedAt", UNSET))


        def _parse_applied_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_by = _parse_applied_by(d.pop("appliedBy", UNSET))


        listing_pricing_history_entry = cls(
            date=date,
            recommended_rate=recommended_rate,
            applied_rate=applied_rate,
            status=status,
            recommendation_factors=recommendation_factors,
            applied_at=applied_at,
            applied_by=applied_by,
        )


        listing_pricing_history_entry.additional_properties = d
        return listing_pricing_history_entry

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
