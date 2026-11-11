from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.error_error_upgrade_plan import ErrorErrorUpgradePlan
from typing import cast






T = TypeVar("T", bound="ErrorErrorUpgrade")



@_attrs_define
class ErrorErrorUpgrade:
    """ The cheapest plan that covers your usage. Present on the monthly quota refusal (`rate_limit_exceeded`, `scope:
    "monthly"`), `credits_exhausted` and `daily_limit_exceeded`. `monthly_price_usd` is exactly what `checkout_url`
    charges for `listings`. `plan: "custom"` means no self-serve plan covers the usage (already on Starter, more than
    Starter's quotas, or more than 100 listings): email `contact_email`.

        Attributes:
            plan (ErrorErrorUpgradePlan):  Example: starter.
            name (str):  Example: Starter.
            monthly_price_usd (float | None): Monthly price in USD for `listings`: Starter's base plus its per-listing
                price. Null for `custom`. Example: 99.
            listings (int | None): Listings the price covers: active plus held back by your plan, across your workspaces.
                Example: 2.
            monthly_requests (int | None): Requests a month the plan includes. Null for `custom`. Example: 100000.
            daily_requests (int | None): The plan's daily request cap. Null for `custom`. Example: 25000.
            checkout_url (None | str): Opens checkout for exactly `monthly_price_usd`. Null for `custom`. Example:
                https://repull.dev/dashboard/billing?upgrade=starter.
            contact_email (None | str): Where to ask for a plan when `plan` is `custom`.
     """

    plan: ErrorErrorUpgradePlan
    name: str
    monthly_price_usd: float | None
    listings: int | None
    monthly_requests: int | None
    daily_requests: int | None
    checkout_url: None | str
    contact_email: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.value

        name = self.name

        monthly_price_usd: float | None
        monthly_price_usd = self.monthly_price_usd

        listings: int | None
        listings = self.listings

        monthly_requests: int | None
        monthly_requests = self.monthly_requests

        daily_requests: int | None
        daily_requests = self.daily_requests

        checkout_url: None | str
        checkout_url = self.checkout_url

        contact_email: None | str
        contact_email = self.contact_email


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "plan": plan,
            "name": name,
            "monthly_price_usd": monthly_price_usd,
            "listings": listings,
            "monthly_requests": monthly_requests,
            "daily_requests": daily_requests,
            "checkout_url": checkout_url,
            "contact_email": contact_email,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan = ErrorErrorUpgradePlan(d.pop("plan"))




        name = d.pop("name")

        def _parse_monthly_price_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        monthly_price_usd = _parse_monthly_price_usd(d.pop("monthly_price_usd"))


        def _parse_listings(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        listings = _parse_listings(d.pop("listings"))


        def _parse_monthly_requests(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monthly_requests = _parse_monthly_requests(d.pop("monthly_requests"))


        def _parse_daily_requests(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        daily_requests = _parse_daily_requests(d.pop("daily_requests"))


        def _parse_checkout_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checkout_url = _parse_checkout_url(d.pop("checkout_url"))


        def _parse_contact_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        contact_email = _parse_contact_email(d.pop("contact_email"))


        error_error_upgrade = cls(
            plan=plan,
            name=name,
            monthly_price_usd=monthly_price_usd,
            listings=listings,
            monthly_requests=monthly_requests,
            daily_requests=daily_requests,
            checkout_url=checkout_url,
            contact_email=contact_email,
        )


        error_error_upgrade.additional_properties = d
        return error_error_upgrade

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
