from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_transaction_status import AirbnbTransactionStatus
from ..models.airbnb_transaction_type import AirbnbTransactionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.airbnb_transaction_guest_breakdown import AirbnbTransactionGuestBreakdown
  from ..models.airbnb_transaction_host_breakdown import AirbnbTransactionHostBreakdown
  from ..models.airbnb_transaction_payout import AirbnbTransactionPayout





T = TypeVar("T", bound="AirbnbTransaction")



@_attrs_define
class AirbnbTransaction:
    """ One Airbnb host transaction — a reservation earning, a settled payout, or a resolution adjustment — with the genuine
    host- and guest-side financial breakdown Airbnb exposes. All money is in host currency; fees and withholding are
    negative (deductions). Two owner-statement concepts are NOT available from Airbnb and are listed in
    `unavailable_fields` rather than fabricated: property-management fee and itemised nightly discounts (the latter are
    already netted into `host_breakdown.accommodation_subtotal`).

        Attributes:
            transaction_id (str): Upstream Airbnb transaction id.
            payout (AirbnbTransactionPayout):
            host_breakdown (AirbnbTransactionHostBreakdown): Host-side breakdown (all host currency).
            guest_breakdown (AirbnbTransactionGuestBreakdown): Guest-side breakdown (what the guest paid).
            unavailable_fields (list[str]): Fields Airbnb does not expose (never fabricated), e.g. `management_fee`,
                `itemized_discounts`.
            type_ (AirbnbTransactionType | Unset): Transaction kind.
            reference (None | str | Unset):
            date (datetime.date | None | Unset): Transaction date.
            confirmation_code (None | str | Unset): Airbnb confirmation code — links this transaction to a reservation.
            reservation_id (int | None | Unset): Resolved Vanio reservation id when the confirmation code matched a
                reservation in this workspace; null otherwise.
            account_id (None | str | Unset): Which connected Airbnb account this transaction belongs to — the Airbnb host
                id, as a string (they exceed 2^53). `null` on rows that name no listing (payouts). Example: 1772489413932732258.
            account_name (None | str | Unset): Display name of that connected Airbnb account. Example: Pomello.
            listing_id (None | str | Unset): Airbnb listing id.
            thread_id (None | str | Unset):
            nights (int | None | Unset):
            reservation_start_date (datetime.date | None | Unset):
            booked_at (datetime.datetime | None | Unset):
            check_in (datetime.datetime | None | Unset):
            check_out (datetime.datetime | None | Unset):
            time_zone (None | str | Unset):
            guest_name (None | str | Unset):
            status (AirbnbTransactionStatus | Unset): Payout status signal: COMPLETED (settled) vs UPCOMING (expected).
            status_type (None | str | Unset):
            currency (None | str | Unset):
            host_currency (None | str | Unset):
            amount (float | None | Unset): Top-level transaction amount.
            standard_fees (Any | Unset): Raw Airbnb standard-fees array.
            tax_details (Any | Unset): Raw Airbnb tax-details object.
            synced_at (datetime.datetime | None | Unset):
     """

    transaction_id: str
    payout: AirbnbTransactionPayout
    host_breakdown: AirbnbTransactionHostBreakdown
    guest_breakdown: AirbnbTransactionGuestBreakdown
    unavailable_fields: list[str]
    type_: AirbnbTransactionType | Unset = UNSET
    reference: None | str | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    account_id: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    thread_id: None | str | Unset = UNSET
    nights: int | None | Unset = UNSET
    reservation_start_date: datetime.date | None | Unset = UNSET
    booked_at: datetime.datetime | None | Unset = UNSET
    check_in: datetime.datetime | None | Unset = UNSET
    check_out: datetime.datetime | None | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    status: AirbnbTransactionStatus | Unset = UNSET
    status_type: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    host_currency: None | str | Unset = UNSET
    amount: float | None | Unset = UNSET
    standard_fees: Any | Unset = UNSET
    tax_details: Any | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_transaction_guest_breakdown import AirbnbTransactionGuestBreakdown
        from ..models.airbnb_transaction_host_breakdown import AirbnbTransactionHostBreakdown
        from ..models.airbnb_transaction_payout import AirbnbTransactionPayout
        transaction_id = self.transaction_id

        payout = self.payout.to_dict()

        host_breakdown = self.host_breakdown.to_dict()

        guest_breakdown = self.guest_breakdown.to_dict()

        unavailable_fields = self.unavailable_fields



        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

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

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        thread_id: None | str | Unset
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        nights: int | None | Unset
        if isinstance(self.nights, Unset):
            nights = UNSET
        else:
            nights = self.nights

        reservation_start_date: None | str | Unset
        if isinstance(self.reservation_start_date, Unset):
            reservation_start_date = UNSET
        elif isinstance(self.reservation_start_date, datetime.date):
            reservation_start_date = self.reservation_start_date.isoformat()
        else:
            reservation_start_date = self.reservation_start_date

        booked_at: None | str | Unset
        if isinstance(self.booked_at, Unset):
            booked_at = UNSET
        elif isinstance(self.booked_at, datetime.datetime):
            booked_at = self.booked_at.isoformat()
        else:
            booked_at = self.booked_at

        check_in: None | str | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        elif isinstance(self.check_in, datetime.datetime):
            check_in = self.check_in.isoformat()
        else:
            check_in = self.check_in

        check_out: None | str | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        elif isinstance(self.check_out, datetime.datetime):
            check_out = self.check_out.isoformat()
        else:
            check_out = self.check_out

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        status_type: None | str | Unset
        if isinstance(self.status_type, Unset):
            status_type = UNSET
        else:
            status_type = self.status_type

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        host_currency: None | str | Unset
        if isinstance(self.host_currency, Unset):
            host_currency = UNSET
        else:
            host_currency = self.host_currency

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        standard_fees = self.standard_fees

        tax_details = self.tax_details

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
            "transaction_id": transaction_id,
            "payout": payout,
            "host_breakdown": host_breakdown,
            "guest_breakdown": guest_breakdown,
            "unavailable_fields": unavailable_fields,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if reference is not UNSET:
            field_dict["reference"] = reference
        if date is not UNSET:
            field_dict["date"] = date
        if confirmation_code is not UNSET:
            field_dict["confirmation_code"] = confirmation_code
        if reservation_id is not UNSET:
            field_dict["reservation_id"] = reservation_id
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if nights is not UNSET:
            field_dict["nights"] = nights
        if reservation_start_date is not UNSET:
            field_dict["reservation_start_date"] = reservation_start_date
        if booked_at is not UNSET:
            field_dict["booked_at"] = booked_at
        if check_in is not UNSET:
            field_dict["check_in"] = check_in
        if check_out is not UNSET:
            field_dict["check_out"] = check_out
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if guest_name is not UNSET:
            field_dict["guest_name"] = guest_name
        if status is not UNSET:
            field_dict["status"] = status
        if status_type is not UNSET:
            field_dict["status_type"] = status_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if host_currency is not UNSET:
            field_dict["host_currency"] = host_currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if standard_fees is not UNSET:
            field_dict["standard_fees"] = standard_fees
        if tax_details is not UNSET:
            field_dict["tax_details"] = tax_details
        if synced_at is not UNSET:
            field_dict["synced_at"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_transaction_guest_breakdown import AirbnbTransactionGuestBreakdown
        from ..models.airbnb_transaction_host_breakdown import AirbnbTransactionHostBreakdown
        from ..models.airbnb_transaction_payout import AirbnbTransactionPayout
        d = dict(src_dict)
        transaction_id = d.pop("transaction_id")

        payout = AirbnbTransactionPayout.from_dict(d.pop("payout"))




        host_breakdown = AirbnbTransactionHostBreakdown.from_dict(d.pop("host_breakdown"))




        guest_breakdown = AirbnbTransactionGuestBreakdown.from_dict(d.pop("guest_breakdown"))




        unavailable_fields = cast(list[str], d.pop("unavailable_fields"))


        _type_ = d.pop("type", UNSET)
        type_: AirbnbTransactionType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = AirbnbTransactionType(_type_)




        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))


        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()



                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmation_code", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservation_id", UNSET))


        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("account_name", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listing_id", UNSET))


        def _parse_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))


        def _parse_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nights = _parse_nights(d.pop("nights", UNSET))


        def _parse_reservation_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reservation_start_date_type_0 = isoparse(data).date()



                return reservation_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        reservation_start_date = _parse_reservation_start_date(d.pop("reservation_start_date", UNSET))


        def _parse_booked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                booked_at_type_0 = isoparse(data)



                return booked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        booked_at = _parse_booked_at(d.pop("booked_at", UNSET))


        def _parse_check_in(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_type_0 = isoparse(data)



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        check_in = _parse_check_in(d.pop("check_in", UNSET))


        def _parse_check_out(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_type_0 = isoparse(data)



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        check_out = _parse_check_out(d.pop("check_out", UNSET))


        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guest_name", UNSET))


        _status = d.pop("status", UNSET)
        status: AirbnbTransactionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AirbnbTransactionStatus(_status)




        def _parse_status_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_type = _parse_status_type(d.pop("status_type", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_host_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_currency = _parse_host_currency(d.pop("host_currency", UNSET))


        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        standard_fees = d.pop("standard_fees", UNSET)

        tax_details = d.pop("tax_details", UNSET)

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

        synced_at = _parse_synced_at(d.pop("synced_at", UNSET))


        airbnb_transaction = cls(
            transaction_id=transaction_id,
            payout=payout,
            host_breakdown=host_breakdown,
            guest_breakdown=guest_breakdown,
            unavailable_fields=unavailable_fields,
            type_=type_,
            reference=reference,
            date=date,
            confirmation_code=confirmation_code,
            reservation_id=reservation_id,
            account_id=account_id,
            account_name=account_name,
            listing_id=listing_id,
            thread_id=thread_id,
            nights=nights,
            reservation_start_date=reservation_start_date,
            booked_at=booked_at,
            check_in=check_in,
            check_out=check_out,
            time_zone=time_zone,
            guest_name=guest_name,
            status=status,
            status_type=status_type,
            currency=currency,
            host_currency=host_currency,
            amount=amount,
            standard_fees=standard_fees,
            tax_details=tax_details,
            synced_at=synced_at,
        )


        airbnb_transaction.additional_properties = d
        return airbnb_transaction

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
