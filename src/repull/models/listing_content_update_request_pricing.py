from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateRequestPricing")



@_attrs_define
class ListingContentUpdateRequestPricing:
    """ The listing's standing rates. Partial like every other section: only the fields you send are written, and `null`
    clears one.

    Changing `defaultDailyPrice` or `weekendPrice` also moves the nights on the calendar that still carry the old rate
    and were written by us — a night you or a channel priced yourself is never touched, and neither is a blocked or
    reserved one. So a price change reaches the calendar without overwriting anyone's work.

    This is still a local write. Publish to send the new rates to a channel.

        Attributes:
            default_daily_price (float | None | Unset): Nightly rate for every night that is not a weekend night.
            weekend_price (float | None | Unset): Nightly rate for Saturday and Sunday nights (UTC).
            cleaning_fee (float | None | Unset):
            price_per_extra_guest (float | None | Unset):
            security_deposit (float | None | Unset):
            weekly_discount (float | None | Unset): A percentage, not a fraction: `10` is 10% off a stay of a week or more.
                A value between 0 and 1 is refused (it would publish as a fraction of one percent) — send `10`, not `0.1`. `0`
                clears it.
            monthly_discount (float | None | Unset): A percentage, not a fraction: `20` is 20% off a stay of 28 nights or
                more. Values between 0 and 1 are refused, as for `weeklyDiscount`.
            guests_included (int | None | Unset): Guests covered by the nightly rate before `pricePerExtraGuest` applies.
            currency (None | str | Unset): ISO 4217, e.g. `USD`.
     """

    default_daily_price: float | None | Unset = UNSET
    weekend_price: float | None | Unset = UNSET
    cleaning_fee: float | None | Unset = UNSET
    price_per_extra_guest: float | None | Unset = UNSET
    security_deposit: float | None | Unset = UNSET
    weekly_discount: float | None | Unset = UNSET
    monthly_discount: float | None | Unset = UNSET
    guests_included: int | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        default_daily_price: float | None | Unset
        if isinstance(self.default_daily_price, Unset):
            default_daily_price = UNSET
        else:
            default_daily_price = self.default_daily_price

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

        price_per_extra_guest: float | None | Unset
        if isinstance(self.price_per_extra_guest, Unset):
            price_per_extra_guest = UNSET
        else:
            price_per_extra_guest = self.price_per_extra_guest

        security_deposit: float | None | Unset
        if isinstance(self.security_deposit, Unset):
            security_deposit = UNSET
        else:
            security_deposit = self.security_deposit

        weekly_discount: float | None | Unset
        if isinstance(self.weekly_discount, Unset):
            weekly_discount = UNSET
        else:
            weekly_discount = self.weekly_discount

        monthly_discount: float | None | Unset
        if isinstance(self.monthly_discount, Unset):
            monthly_discount = UNSET
        else:
            monthly_discount = self.monthly_discount

        guests_included: int | None | Unset
        if isinstance(self.guests_included, Unset):
            guests_included = UNSET
        else:
            guests_included = self.guests_included

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default_daily_price is not UNSET:
            field_dict["defaultDailyPrice"] = default_daily_price
        if weekend_price is not UNSET:
            field_dict["weekendPrice"] = weekend_price
        if cleaning_fee is not UNSET:
            field_dict["cleaningFee"] = cleaning_fee
        if price_per_extra_guest is not UNSET:
            field_dict["pricePerExtraGuest"] = price_per_extra_guest
        if security_deposit is not UNSET:
            field_dict["securityDeposit"] = security_deposit
        if weekly_discount is not UNSET:
            field_dict["weeklyDiscount"] = weekly_discount
        if monthly_discount is not UNSET:
            field_dict["monthlyDiscount"] = monthly_discount
        if guests_included is not UNSET:
            field_dict["guestsIncluded"] = guests_included
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_default_daily_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_daily_price = _parse_default_daily_price(d.pop("defaultDailyPrice", UNSET))


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


        def _parse_price_per_extra_guest(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_per_extra_guest = _parse_price_per_extra_guest(d.pop("pricePerExtraGuest", UNSET))


        def _parse_security_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        security_deposit = _parse_security_deposit(d.pop("securityDeposit", UNSET))


        def _parse_weekly_discount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weekly_discount = _parse_weekly_discount(d.pop("weeklyDiscount", UNSET))


        def _parse_monthly_discount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_discount = _parse_monthly_discount(d.pop("monthlyDiscount", UNSET))


        def _parse_guests_included(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guests_included = _parse_guests_included(d.pop("guestsIncluded", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        listing_content_update_request_pricing = cls(
            default_daily_price=default_daily_price,
            weekend_price=weekend_price,
            cleaning_fee=cleaning_fee,
            price_per_extra_guest=price_per_extra_guest,
            security_deposit=security_deposit,
            weekly_discount=weekly_discount,
            monthly_discount=monthly_discount,
            guests_included=guests_included,
            currency=currency,
        )


        listing_content_update_request_pricing.additional_properties = d
        return listing_content_update_request_pricing

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
