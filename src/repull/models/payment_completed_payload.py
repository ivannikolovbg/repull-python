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






T = TypeVar("T", bound="PaymentCompletedPayload")



@_attrs_define
class PaymentCompletedPayload:
    """ Payload for `payment.completed`. A guest payment was successfully captured.

        Attributes:
            id (str | Unset):  Example: pay_01HX5XPQ2K.
            reservation_id (int | Unset):  Example: 215906.
            amount (str | Unset):  Example: 1320.00.
            currency (str | Unset):  Example: USD.
            method (str | Unset):  Example: card.
            captured_at (datetime.datetime | Unset):  Example: 2026-05-01T12:35:00.000Z.
     """

    id: str | Unset = UNSET
    reservation_id: int | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    method: str | Unset = UNSET
    captured_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reservation_id = self.reservation_id

        amount = self.amount

        currency = self.currency

        method = self.method

        captured_at: str | Unset = UNSET
        if not isinstance(self.captured_at, Unset):
            captured_at = self.captured_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if method is not UNSET:
            field_dict["method"] = method
        if captured_at is not UNSET:
            field_dict["capturedAt"] = captured_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        reservation_id = d.pop("reservationId", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        method = d.pop("method", UNSET)

        _captured_at = d.pop("capturedAt", UNSET)
        captured_at: datetime.datetime | Unset
        if isinstance(_captured_at,  Unset):
            captured_at = UNSET
        else:
            captured_at = isoparse(_captured_at)




        payment_completed_payload = cls(
            id=id,
            reservation_id=reservation_id,
            amount=amount,
            currency=currency,
            method=method,
            captured_at=captured_at,
        )


        payment_completed_payload.additional_properties = d
        return payment_completed_payload

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
