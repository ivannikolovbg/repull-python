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






T = TypeVar("T", bound="PaymentRefundedPayload")



@_attrs_define
class PaymentRefundedPayload:
    """ Payload for `payment.refunded`. A previous payment was refunded in part or in full.

        Attributes:
            id (str | Unset):  Example: pay_01HX5XPQ2K.
            refund_id (str | Unset):  Example: rfn_01HX5XPQ2K.
            reservation_id (int | Unset):  Example: 215906.
            amount (str | Unset):  Example: 1320.00.
            currency (str | Unset):  Example: USD.
            refunded_at (datetime.datetime | Unset):  Example: 2026-05-01T19:00:00.000Z.
     """

    id: str | Unset = UNSET
    refund_id: str | Unset = UNSET
    reservation_id: int | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    refunded_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        refund_id = self.refund_id

        reservation_id = self.reservation_id

        amount = self.amount

        currency = self.currency

        refunded_at: str | Unset = UNSET
        if not isinstance(self.refunded_at, Unset):
            refunded_at = self.refunded_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if refund_id is not UNSET:
            field_dict["refundId"] = refund_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if refunded_at is not UNSET:
            field_dict["refundedAt"] = refunded_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        refund_id = d.pop("refundId", UNSET)

        reservation_id = d.pop("reservationId", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _refunded_at = d.pop("refundedAt", UNSET)
        refunded_at: datetime.datetime | Unset
        if isinstance(_refunded_at,  Unset):
            refunded_at = UNSET
        else:
            refunded_at = isoparse(_refunded_at)




        payment_refunded_payload = cls(
            id=id,
            refund_id=refund_id,
            reservation_id=reservation_id,
            amount=amount,
            currency=currency,
            refunded_at=refunded_at,
        )


        payment_refunded_payload.additional_properties = d
        return payment_refunded_payload

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
