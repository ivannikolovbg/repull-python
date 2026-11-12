from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.billing_notice_code import BillingNoticeCode
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="BillingNotice")



@_attrs_define
class BillingNotice:
    """ Added to the body of every successful (2xx) JSON object response while the plan's last renewal payment failed (the
    subscription is past_due or unpaid). It never blocks a request: API access keeps working while Stripe retries the
    card. Tell the user: pay the invoice at `payUrl`, or update the card at `billingUrl`. It disappears once the invoice
    is paid.

        Attributes:
            code (BillingNoticeCode): "payment_failed": the last renewal payment failed and is still owed.
            amount (float | None): The amount owed, in major units of `currency`. Example: 99.
            currency (str): Lower-case ISO 4217 code. Example: usd.
            failed_at (datetime.datetime | None): When the payment failed. Example: 2026-11-12T14:52:17.000Z.
            next_retry_at (datetime.datetime | None): When Stripe retries the card automatically; null when no retry is
                left. Example: 2026-11-14T20:52:16.000Z.
            pay_url (None | str): Stripe's hosted invoice: pay it there with any card. Example:
                https://invoice.stripe.com/i/acct_1TUV6uDYjA8GNo6e/live_abc.
            message (str):  Example: Your $99.00 Repull plan payment failed on Nov 12, 2026. Your API calls keep working.
                Stripe retries the card automatically on Nov 14, 2026..
            fix (str):  Example: Pay the invoice at `payUrl`, or update the card at https://repull.dev/dashboard/billing
                (Manage billing) so the next retry goes through. This notice disappears once it is paid..
            billing_url (str):  Example: https://repull.dev/dashboard/billing.
     """

    code: BillingNoticeCode
    amount: float | None
    currency: str
    failed_at: datetime.datetime | None
    next_retry_at: datetime.datetime | None
    pay_url: None | str
    message: str
    fix: str
    billing_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        amount: float | None
        amount = self.amount

        currency = self.currency

        failed_at: None | str
        if isinstance(self.failed_at, datetime.datetime):
            failed_at = self.failed_at.isoformat()
        else:
            failed_at = self.failed_at

        next_retry_at: None | str
        if isinstance(self.next_retry_at, datetime.datetime):
            next_retry_at = self.next_retry_at.isoformat()
        else:
            next_retry_at = self.next_retry_at

        pay_url: None | str
        pay_url = self.pay_url

        message = self.message

        fix = self.fix

        billing_url = self.billing_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "amount": amount,
            "currency": currency,
            "failedAt": failed_at,
            "nextRetryAt": next_retry_at,
            "payUrl": pay_url,
            "message": message,
            "fix": fix,
            "billingUrl": billing_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = BillingNoticeCode(d.pop("code"))




        def _parse_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        amount = _parse_amount(d.pop("amount"))


        currency = d.pop("currency")

        def _parse_failed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failed_at_type_0 = isoparse(data)



                return failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        failed_at = _parse_failed_at(d.pop("failedAt"))


        def _parse_next_retry_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_retry_at_type_0 = isoparse(data)



                return next_retry_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_retry_at = _parse_next_retry_at(d.pop("nextRetryAt"))


        def _parse_pay_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pay_url = _parse_pay_url(d.pop("payUrl"))


        message = d.pop("message")

        fix = d.pop("fix")

        billing_url = d.pop("billingUrl")

        billing_notice = cls(
            code=code,
            amount=amount,
            currency=currency,
            failed_at=failed_at,
            next_retry_at=next_retry_at,
            pay_url=pay_url,
            message=message,
            fix=fix,
            billing_url=billing_url,
        )


        billing_notice.additional_properties = d
        return billing_notice

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
