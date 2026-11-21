from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_pricing_response_200_data_nightly_rate_type_0 import UpdateVrboListingPricingResponse200DataNightlyRateType0





T = TypeVar("T", bound="UpdateVrboListingPricingResponse200Data")



@_attrs_define
class UpdateVrboListingPricingResponse200Data:
    """ What Vrbo has after the write, read back from Vrbo.

        Attributes:
            currency (None | str | Unset):
            nightly_rate (None | Unset | UpdateVrboListingPricingResponse200DataNightlyRateType0): Base rate per weekday
                (sunday … saturday).
            weekly_discount_percent (float | None | Unset):
            monthly_discount_percent (float | None | Unset):
            default_min_stay (int | None | Unset):
            rate_limits (Any | Unset):
     """

    currency: None | str | Unset = UNSET
    nightly_rate: None | Unset | UpdateVrboListingPricingResponse200DataNightlyRateType0 = UNSET
    weekly_discount_percent: float | None | Unset = UNSET
    monthly_discount_percent: float | None | Unset = UNSET
    default_min_stay: int | None | Unset = UNSET
    rate_limits: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_pricing_response_200_data_nightly_rate_type_0 import UpdateVrboListingPricingResponse200DataNightlyRateType0
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        nightly_rate: dict[str, Any] | None | Unset
        if isinstance(self.nightly_rate, Unset):
            nightly_rate = UNSET
        elif isinstance(self.nightly_rate, UpdateVrboListingPricingResponse200DataNightlyRateType0):
            nightly_rate = self.nightly_rate.to_dict()
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

        default_min_stay: int | None | Unset
        if isinstance(self.default_min_stay, Unset):
            default_min_stay = UNSET
        else:
            default_min_stay = self.default_min_stay

        rate_limits = self.rate_limits


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if nightly_rate is not UNSET:
            field_dict["nightlyRate"] = nightly_rate
        if weekly_discount_percent is not UNSET:
            field_dict["weeklyDiscountPercent"] = weekly_discount_percent
        if monthly_discount_percent is not UNSET:
            field_dict["monthlyDiscountPercent"] = monthly_discount_percent
        if default_min_stay is not UNSET:
            field_dict["defaultMinStay"] = default_min_stay
        if rate_limits is not UNSET:
            field_dict["rateLimits"] = rate_limits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_pricing_response_200_data_nightly_rate_type_0 import UpdateVrboListingPricingResponse200DataNightlyRateType0
        d = dict(src_dict)
        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_nightly_rate(data: object) -> None | Unset | UpdateVrboListingPricingResponse200DataNightlyRateType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nightly_rate_type_0 = UpdateVrboListingPricingResponse200DataNightlyRateType0.from_dict(data)



                return nightly_rate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingPricingResponse200DataNightlyRateType0, data)

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


        def _parse_default_min_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_min_stay = _parse_default_min_stay(d.pop("defaultMinStay", UNSET))


        rate_limits = d.pop("rateLimits", UNSET)

        update_vrbo_listing_pricing_response_200_data = cls(
            currency=currency,
            nightly_rate=nightly_rate,
            weekly_discount_percent=weekly_discount_percent,
            monthly_discount_percent=monthly_discount_percent,
            default_min_stay=default_min_stay,
            rate_limits=rate_limits,
        )


        update_vrbo_listing_pricing_response_200_data.additional_properties = d
        return update_vrbo_listing_pricing_response_200_data

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
