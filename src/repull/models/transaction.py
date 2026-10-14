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
  from ..models.transaction_fees import TransactionFees
  from ..models.transaction_payout import TransactionPayout





T = TypeVar("T", bound="Transaction")



@_attrs_define
class Transaction:
    """ One row of the unified transactions & payments ledger: a payout (`isPayout: true`) or a reservation charge / refund,
    on any channel. `platform` is normalized — `booking` is Booking.com however the account was connected (never
    `booking_extranet`). For a payout, `amount` is the net the host received, `grossAmount` the guest-paid gross, and
    `fees` the deductions (commission, payments service fee, processing fee).

        Attributes:
            transaction_id (None | str): Stable id of the transaction (the underlying payment id). Upsert on it. Example:
                booking_payout_5463377687_bank_transfer.
            platform (None | str): Normalized channel: `airbnb`, `booking` (Booking.com, however connected — never
                `booking_extranet`), or `vrbo`. Example: booking.
            is_payout (bool): `true` when this is money that reached the host (a payout).
            fees (TransactionFees):
            payout (TransactionPayout):
            type_ (None | str | Unset): Transaction type: `Payout`, `Reservation`, `Refund`, … Example: Payout.
            status (None | str | Unset): Normalized settlement status (`COMPLETED` / `UPCOMING`; the raw value passes
                through when it maps to neither). Example: COMPLETED.
            date (None | str | Unset): Transaction / payout date (the channel's display form or ISO). Example: 27 Aug 2026.
            currency (None | str | Unset):  Example: NOK.
            amount (float | None | Unset): Net amount; for a payout, what the host received. Example: 18597.12.
            gross_amount (float | None | Unset): Guest-paid gross (payouts). Example: 22272.
            confirmation_code (None | str | Unset):  Example: 5463377687.
            reservation_id (int | None | Unset):
            listing_id (int | None | Unset):
            synced_at (datetime.datetime | None | Unset):
     """

    transaction_id: None | str
    platform: None | str
    is_payout: bool
    fees: TransactionFees
    payout: TransactionPayout
    type_: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    date: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    amount: float | None | Unset = UNSET
    gross_amount: float | None | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    listing_id: int | None | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_fees import TransactionFees
        from ..models.transaction_payout import TransactionPayout
        transaction_id: None | str
        transaction_id = self.transaction_id

        platform: None | str
        platform = self.platform

        is_payout = self.is_payout

        fees = self.fees.to_dict()

        payout = self.payout.to_dict()

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        gross_amount: float | None | Unset
        if isinstance(self.gross_amount, Unset):
            gross_amount = UNSET
        else:
            gross_amount = self.gross_amount

        confirmation_code: None | str | Unset
        if isinstance(self.confirmation_code, Unset):
            confirmation_code = UNSET
        else:
            confirmation_code = self.confirmation_code

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        elif isinstance(self.synced_at, datetime.datetime):
            synced_at = self.synced_at.isoformat()
        else:
            synced_at = self.synced_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "transactionId": transaction_id,
            "platform": platform,
            "isPayout": is_payout,
            "fees": fees,
            "payout": payout,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if date is not UNSET:
            field_dict["date"] = date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if gross_amount is not UNSET:
            field_dict["grossAmount"] = gross_amount
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_fees import TransactionFees
        from ..models.transaction_payout import TransactionPayout
        d = dict(src_dict)
        def _parse_transaction_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId"))


        def _parse_platform(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        platform = _parse_platform(d.pop("platform"))


        is_payout = d.pop("isPayout")

        fees = TransactionFees.from_dict(d.pop("fees"))




        payout = TransactionPayout.from_dict(d.pop("payout"))




        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_gross_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gross_amount = _parse_gross_amount(d.pop("grossAmount", UNSET))


        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmationCode", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_at_type_0 = isoparse(data)



                return synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        synced_at = _parse_synced_at(d.pop("syncedAt", UNSET))


        transaction = cls(
            transaction_id=transaction_id,
            platform=platform,
            is_payout=is_payout,
            fees=fees,
            payout=payout,
            type_=type_,
            status=status,
            date=date,
            currency=currency,
            amount=amount,
            gross_amount=gross_amount,
            confirmation_code=confirmation_code,
            reservation_id=reservation_id,
            listing_id=listing_id,
            synced_at=synced_at,
        )


        transaction.additional_properties = d
        return transaction

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
