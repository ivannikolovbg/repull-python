from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TransactionPayout")



@_attrs_define
class TransactionPayout:
    """ 
        Attributes:
            payout_id (None | str): Reference of the payout this row belongs to. Example: gkvDj0Jm9ZaA6IiO.
            payout_date (None | str):
            paid_out_amount (float | None): On a payout row: the net paid out to the host. Example: 18597.12.
            bank_destination (None | str | Unset): Masked destination bank account the payout was sent to (Booking.com
                payouts, from the statement PDF). Null on channels/rows without one. Example: NO***********404.
            statement_url (None | str | Unset): Repull-hosted download link for the original payout statement PDF (the
                authoritative settlement record). Add `?format=csv` for the CSV. Served by `GET /v1/transactions/{id}/statement`
                — no channel session needed. Null when none is stored.
            statement_id (None | str | Unset): The channel's own numeric statement id (Booking.com, e.g. "010747030095").
                Null when none. Example: 010747030095.
     """

    payout_id: None | str
    payout_date: None | str
    paid_out_amount: float | None
    bank_destination: None | str | Unset = UNSET
    statement_url: None | str | Unset = UNSET
    statement_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payout_id: None | str
        payout_id = self.payout_id

        payout_date: None | str
        payout_date = self.payout_date

        paid_out_amount: float | None
        paid_out_amount = self.paid_out_amount

        bank_destination: None | str | Unset
        if isinstance(self.bank_destination, Unset):
            bank_destination = UNSET
        else:
            bank_destination = self.bank_destination

        statement_url: None | str | Unset
        if isinstance(self.statement_url, Unset):
            statement_url = UNSET
        else:
            statement_url = self.statement_url

        statement_id: None | str | Unset
        if isinstance(self.statement_id, Unset):
            statement_id = UNSET
        else:
            statement_id = self.statement_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "payoutId": payout_id,
            "payoutDate": payout_date,
            "paidOutAmount": paid_out_amount,
        })
        if bank_destination is not UNSET:
            field_dict["bankDestination"] = bank_destination
        if statement_url is not UNSET:
            field_dict["statementUrl"] = statement_url
        if statement_id is not UNSET:
            field_dict["statementId"] = statement_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_payout_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payout_id = _parse_payout_id(d.pop("payoutId"))


        def _parse_payout_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payout_date = _parse_payout_date(d.pop("payoutDate"))


        def _parse_paid_out_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        paid_out_amount = _parse_paid_out_amount(d.pop("paidOutAmount"))


        def _parse_bank_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_destination = _parse_bank_destination(d.pop("bankDestination", UNSET))


        def _parse_statement_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statement_url = _parse_statement_url(d.pop("statementUrl", UNSET))


        def _parse_statement_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statement_id = _parse_statement_id(d.pop("statementId", UNSET))


        transaction_payout = cls(
            payout_id=payout_id,
            payout_date=payout_date,
            paid_out_amount=paid_out_amount,
            bank_destination=bank_destination,
            statement_url=statement_url,
            statement_id=statement_id,
        )


        transaction_payout.additional_properties = d
        return transaction_payout

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
