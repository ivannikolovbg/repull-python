from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plan_notice_code import PlanNoticeCode
from typing import cast






T = TypeVar("T", bound="PlanNotice")



@_attrs_define
class PlanNotice:
    """ Added to the body of EVERY JSON response (success or error, except bare arrays and 5xx) while the workspace is
    connected to more listings than its plan lets it use — so a developer reading any payload, or an AI assistant
    relaying it, sees it. Connect keeps every listing it finds, but on a capped plan only as many as the plan allows are
    active; the rest are held back inactive and keep syncing. The same responses also carry the `X-Repull-Listings-Held-
    Back` and `X-Repull-Active-Listing-Limit` headers. Using a held-back listing answers `403 listing_inactive` with
    `reason: "plan_limit"`. Tell the user: they can see the held-back listings with `GET /v1/listings?status=all`,
    choose which are active with `POST /v1/listings/status`, or upgrade.

        Attributes:
            code (PlanNoticeCode):
            listings_held_back (int): Connected listings kept inactive because of the plan. Example: 40.
            active_listing_limit (int | None): The plan's cap on active listings. Example: 3.
            message (str):  Example: 40 more connected listings are held inactive because your plan allows 3 active
                listings. They stay connected and keep syncing..
            fix (str):
            billing_url (str):  Example: https://repull.dev/dashboard/billing.
     """

    code: PlanNoticeCode
    listings_held_back: int
    active_listing_limit: int | None
    message: str
    fix: str
    billing_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        listings_held_back = self.listings_held_back

        active_listing_limit: int | None
        active_listing_limit = self.active_listing_limit

        message = self.message

        fix = self.fix

        billing_url = self.billing_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "listingsHeldBack": listings_held_back,
            "activeListingLimit": active_listing_limit,
            "message": message,
            "fix": fix,
            "billingUrl": billing_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = PlanNoticeCode(d.pop("code"))




        listings_held_back = d.pop("listingsHeldBack")

        def _parse_active_listing_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        active_listing_limit = _parse_active_listing_limit(d.pop("activeListingLimit"))


        message = d.pop("message")

        fix = d.pop("fix")

        billing_url = d.pop("billingUrl")

        plan_notice = cls(
            code=code,
            listings_held_back=listings_held_back,
            active_listing_limit=active_listing_limit,
            message=message,
            fix=fix,
            billing_url=billing_url,
        )


        plan_notice.additional_properties = d
        return plan_notice

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
