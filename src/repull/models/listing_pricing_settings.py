from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingPricingSettings")



@_attrs_define
class ListingPricingSettings:
    """ The listing's standing prices. Nightly rates per date are on `GET /v1/availability/{propertyId}`.

        Attributes:
            currency (None | str | Unset):  Example: GBP.
            base_price (float | None | Unset): Default nightly rate.
            weekend_price (float | None | Unset):
            cleaning_fee (float | None | Unset):
            extra_guest_fee (float | None | Unset): Per extra guest per night, above `guestsIncluded`.
            guests_included (int | None | Unset):
            security_deposit (float | None | Unset):
            weekly_discount_percent (float | None | Unset): Percent off for 7+ nights: `10` is 10%.
            monthly_discount_percent (float | None | Unset): Percent off for 28+ nights.
     """

    currency: None | str | Unset = UNSET
    base_price: float | None | Unset = UNSET
    weekend_price: float | None | Unset = UNSET
    cleaning_fee: float | None | Unset = UNSET
    extra_guest_fee: float | None | Unset = UNSET
    guests_included: int | None | Unset = UNSET
    security_deposit: float | None | Unset = UNSET
    weekly_discount_percent: float | None | Unset = UNSET
    monthly_discount_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        base_price: float | None | Unset
        if isinstance(self.base_price, Unset):
            base_price = UNSET
        else:
            base_price = self.base_price

        weekend_price: float | None | Unset
        if isinstance(self.weekend_price, Unset):
            weekend_price = UNSET
        else:
            weekend_price = self.weekend_price

        cleaning_fee: float | None | Unset
        if isinstance(self.cleaning_fee, Unset):
            cleaning_fee = UNSET
        else:
            cleaning_fee = self.cleaning_fee

        extra_guest_fee: float | None | Unset
        if isinstance(self.extra_guest_fee, Unset):
            extra_guest_fee = UNSET
        else:
            extra_guest_fee = self.extra_guest_fee

        guests_included: int | None | Unset
        if isinstance(self.guests_included, Unset):
            guests_included = UNSET
        else:
            guests_included = self.guests_included

        security_deposit: float | None | Unset
        if isinstance(self.security_deposit, Unset):
            security_deposit = UNSET
        else:
            security_deposit = self.security_deposit

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if weekend_price is not UNSET:
            field_dict["weekendPrice"] = weekend_price
        if cleaning_fee is not UNSET:
            field_dict["cleaningFee"] = cleaning_fee
        if extra_guest_fee is not UNSET:
            field_dict["extraGuestFee"] = extra_guest_fee
        if guests_included is not UNSET:
            field_dict["guestsIncluded"] = guests_included
        if security_deposit is not UNSET:
            field_dict["securityDeposit"] = security_deposit
        if weekly_discount_percent is not UNSET:
            field_dict["weeklyDiscountPercent"] = weekly_discount_percent
        if monthly_discount_percent is not UNSET:
            field_dict["monthlyDiscountPercent"] = monthly_discount_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_base_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        base_price = _parse_base_price(d.pop("basePrice", UNSET))


        def _parse_weekend_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weekend_price = _parse_weekend_price(d.pop("weekendPrice", UNSET))


        def _parse_cleaning_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cleaning_fee = _parse_cleaning_fee(d.pop("cleaningFee", UNSET))


        def _parse_extra_guest_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        extra_guest_fee = _parse_extra_guest_fee(d.pop("extraGuestFee", UNSET))


        def _parse_guests_included(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guests_included = _parse_guests_included(d.pop("guestsIncluded", UNSET))


        def _parse_security_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        security_deposit = _parse_security_deposit(d.pop("securityDeposit", UNSET))


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


        listing_pricing_settings = cls(
            currency=currency,
            base_price=base_price,
            weekend_price=weekend_price,
            cleaning_fee=cleaning_fee,
            extra_guest_fee=extra_guest_fee,
            guests_included=guests_included,
            security_deposit=security_deposit,
            weekly_discount_percent=weekly_discount_percent,
            monthly_discount_percent=monthly_discount_percent,
        )


        listing_pricing_settings.additional_properties = d
        return listing_pricing_settings

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
