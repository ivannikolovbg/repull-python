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
  from ..models.update_vrbo_listing_rates_body_nightly_rates import UpdateVrboListingRatesBodyNightlyRates





T = TypeVar("T", bound="UpdateVrboListingRatesBody")



@_attrs_define
class UpdateVrboListingRatesBody:
    """ 
        Attributes:
            start_date (datetime.date):
            end_date (datetime.date): On or after `startDate`, at most 3 years later.
            nightly_rate (float | Unset): One price for every night in the range.
            nightly_rates (UpdateVrboListingRatesBodyNightlyRates | Unset): A price per weekday; every weekday in the range
                needs one.
            weekly_discount_percent (float | Unset): Stays of 7–27 nights.
            monthly_discount_percent (float | Unset): Stays of 28 nights or more.
     """

    start_date: datetime.date
    end_date: datetime.date
    nightly_rate: float | Unset = UNSET
    nightly_rates: UpdateVrboListingRatesBodyNightlyRates | Unset = UNSET
    weekly_discount_percent: float | Unset = UNSET
    monthly_discount_percent: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_rates_body_nightly_rates import UpdateVrboListingRatesBodyNightlyRates
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        nightly_rate = self.nightly_rate

        nightly_rates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nightly_rates, Unset):
            nightly_rates = self.nightly_rates.to_dict()

        weekly_discount_percent = self.weekly_discount_percent

        monthly_discount_percent = self.monthly_discount_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "startDate": start_date,
            "endDate": end_date,
        })
        if nightly_rate is not UNSET:
            field_dict["nightlyRate"] = nightly_rate
        if nightly_rates is not UNSET:
            field_dict["nightlyRates"] = nightly_rates
        if weekly_discount_percent is not UNSET:
            field_dict["weeklyDiscountPercent"] = weekly_discount_percent
        if monthly_discount_percent is not UNSET:
            field_dict["monthlyDiscountPercent"] = monthly_discount_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_rates_body_nightly_rates import UpdateVrboListingRatesBodyNightlyRates
        d = dict(src_dict)
        start_date = isoparse(d.pop("startDate")).date()




        end_date = isoparse(d.pop("endDate")).date()




        nightly_rate = d.pop("nightlyRate", UNSET)

        _nightly_rates = d.pop("nightlyRates", UNSET)
        nightly_rates: UpdateVrboListingRatesBodyNightlyRates | Unset
        if isinstance(_nightly_rates,  Unset):
            nightly_rates = UNSET
        else:
            nightly_rates = UpdateVrboListingRatesBodyNightlyRates.from_dict(_nightly_rates)




        weekly_discount_percent = d.pop("weeklyDiscountPercent", UNSET)

        monthly_discount_percent = d.pop("monthlyDiscountPercent", UNSET)

        update_vrbo_listing_rates_body = cls(
            start_date=start_date,
            end_date=end_date,
            nightly_rate=nightly_rate,
            nightly_rates=nightly_rates,
            weekly_discount_percent=weekly_discount_percent,
            monthly_discount_percent=monthly_discount_percent,
        )

        return update_vrbo_listing_rates_body

