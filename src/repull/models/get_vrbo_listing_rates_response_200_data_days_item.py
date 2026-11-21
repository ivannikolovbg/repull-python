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






T = TypeVar("T", bound="GetVrboListingRatesResponse200DataDaysItem")



@_attrs_define
class GetVrboListingRatesResponse200DataDaysItem:
    """ 
        Attributes:
            date (datetime.date | Unset):
            weekday (str | Unset):  Example: friday.
            nightly_rate (float | None | Unset):
            weekly_discount_percent (float | None | Unset):
            monthly_discount_percent (float | None | Unset):
            min_stay (int | None | Unset):
     """

    date: datetime.date | Unset = UNSET
    weekday: str | Unset = UNSET
    nightly_rate: float | None | Unset = UNSET
    weekly_discount_percent: float | None | Unset = UNSET
    monthly_discount_percent: float | None | Unset = UNSET
    min_stay: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        weekday = self.weekday

        nightly_rate: float | None | Unset
        if isinstance(self.nightly_rate, Unset):
            nightly_rate = UNSET
        else:
            nightly_rate = self.nightly_rate

        weekly_discount_percent: float | None | Unset
        if isinstance(self.weekly_discount_percent, Unset):
            weekly_discount_percent = UNSET
        else:
            weekly_discount_percent = self.weekly_discount_percent

        monthly_discount_percent: float | None | Unset
        if isinstance(self.monthly_discount_percent, Unset):
            monthly_discount_percent = UNSET
        else:
            monthly_discount_percent = self.monthly_discount_percent

        min_stay: int | None | Unset
        if isinstance(self.min_stay, Unset):
            min_stay = UNSET
        else:
            min_stay = self.min_stay


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if weekday is not UNSET:
            field_dict["weekday"] = weekday
        if nightly_rate is not UNSET:
            field_dict["nightlyRate"] = nightly_rate
        if weekly_discount_percent is not UNSET:
            field_dict["weeklyDiscountPercent"] = weekly_discount_percent
        if monthly_discount_percent is not UNSET:
            field_dict["monthlyDiscountPercent"] = monthly_discount_percent
        if min_stay is not UNSET:
            field_dict["minStay"] = min_stay

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        weekday = d.pop("weekday", UNSET)

        def _parse_nightly_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nightly_rate = _parse_nightly_rate(d.pop("nightlyRate", UNSET))


        def _parse_weekly_discount_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weekly_discount_percent = _parse_weekly_discount_percent(d.pop("weeklyDiscountPercent", UNSET))


        def _parse_monthly_discount_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_discount_percent = _parse_monthly_discount_percent(d.pop("monthlyDiscountPercent", UNSET))


        def _parse_min_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_stay = _parse_min_stay(d.pop("minStay", UNSET))


        get_vrbo_listing_rates_response_200_data_days_item = cls(
            date=date,
            weekday=weekday,
            nightly_rate=nightly_rate,
            weekly_discount_percent=weekly_discount_percent,
            monthly_discount_percent=monthly_discount_percent,
            min_stay=min_stay,
        )


        get_vrbo_listing_rates_response_200_data_days_item.additional_properties = d
        return get_vrbo_listing_rates_response_200_data_days_item

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
