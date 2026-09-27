from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_transaction_status import AirbnbTransactionStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.airbnb_transaction_fees import AirbnbTransactionFees
  from ..models.airbnb_transaction_payout import AirbnbTransactionPayout





T = TypeVar("T", bound="AirbnbTransaction")



@_attrs_define
class AirbnbTransaction:
    """ One line of the Airbnb settlement ledger: a Payout row (`isPayout: true`) or a line it paid. Money is in the payout
    currency; `amount` is signed (negative = taken back, e.g. an adjustment offset against this payout). A payout's
    lines sum to its `payout.paidOutAmount`.

        Attributes:
            transaction_id (str): Stable id. A Payout row: Airbnb's payout id. A settled line:
                `<payoutId>:<type>:<confirmationCode>:<n>`. An upcoming line:
                `upcoming:<accountId>:<type>:<confirmationCode>:<date>:<n>`. Identical on every refresh; upsert on it. Example:
                M-HQLLNSWKUWK7R:reservation:HMRQ8FC4YN:1.
            status (AirbnbTransactionStatus): `COMPLETED`: settled in a payout. `UPCOMING`: expected, not paid out yet.
            type_ (str): Airbnb's line type, verbatim: `Payout`, `Reservation`, `Adjustment`, `Resolution Payout`,
                `Resolution Adjustment`, `Cancellation Fee`, `Pass Through Tot`, … Example: Reservation.
            is_payout (bool): `true` on the Payout row itself.
            fees (AirbnbTransactionFees):
            payout (AirbnbTransactionPayout):
            on_inactive_listing (bool): `true` when the line is on a listing that is inactive in Repull. Still returned, so
                the payout reconciles.
            unavailable_fields (list[str]): What Airbnb's transaction history does not carry, so it is never filled in:
                `taxes` (those Airbnb remits itself; pass-through tax paid to the host arrives as `Pass Through Tot` lines),
                `guest_paid_total`, `original_transaction_id`, `currency_conversion`, `management_fee`.
            account_id (None | str | Unset): The connected Airbnb account (host id, as a string — they exceed 2^53).
                Example: 10000001.
            account_name (None | str | Unset):  Example: Seaside Stays.
            date (datetime.date | None | Unset): The line's date as Airbnb reports it. Can be the day before its payout's
                date.
            currency (None | str | Unset):  Example: USD.
            amount (float | None | Unset): Signed amount this line contributes to its payout, after Airbnb's host service
                fee. On a Payout row, the amount paid out. Example: 40.6.
            gross_amount (float | None | Unset): Before Airbnb's host service fee: `amount - fees.hostServiceFee`. Example:
                48.05.
            confirmation_code (None | str | Unset):  Example: HMRQ8FC4YN.
            reservation_id (None | str | Unset): Repull reservation id when the confirmation code matches a reservation in
                this workspace; `null` when it does not (explicitly unlinked).
            listing_id (None | str | Unset): Airbnb listing id.
            listing_name (None | str | Unset):
            guest_name (None | str | Unset):
            nights (int | None | Unset):
            reservation_start_date (datetime.date | None | Unset):
            description (None | str | Unset): Airbnb's description: the stay dates, the resolution, or on a Payout row the
                payout method.
            reference (None | str | Unset): The resolution id on resolution payouts and adjustments; else `null`. Example:
                CLSF-06472635.
            synced_at (datetime.datetime | None | Unset):
     """

    transaction_id: str
    status: AirbnbTransactionStatus
    type_: str
    is_payout: bool
    fees: AirbnbTransactionFees
    payout: AirbnbTransactionPayout
    on_inactive_listing: bool
    unavailable_fields: list[str]
    account_id: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    amount: float | None | Unset = UNSET
    gross_amount: float | None | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    reservation_id: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    listing_name: None | str | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    nights: int | None | Unset = UNSET
    reservation_start_date: datetime.date | None | Unset = UNSET
    description: None | str | Unset = UNSET
    reference: None | str | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_transaction_fees import AirbnbTransactionFees
        from ..models.airbnb_transaction_payout import AirbnbTransactionPayout
        transaction_id = self.transaction_id

        status = self.status.value

        type_ = self.type_

        is_payout = self.is_payout

        fees = self.fees.to_dict()

        payout = self.payout.to_dict()

        on_inactive_listing = self.on_inactive_listing

        unavailable_fields = self.unavailable_fields



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

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
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

        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        listing_name: None | str | Unset
        if isinstance(self.listing_name, Unset):
            listing_name = UNSET
        else:
            listing_name = self.listing_name

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

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
            "status": status,
            "type": type_,
            "isPayout": is_payout,
            "fees": fees,
            "payout": payout,
            "onInactiveListing": on_inactive_listing,
            "unavailableFields": unavailable_fields,
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
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
        if listing_name is not UNSET:
            field_dict["listingName"] = listing_name
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if nights is not UNSET:
            field_dict["nights"] = nights
        if reservation_start_date is not UNSET:
            field_dict["reservationStartDate"] = reservation_start_date
        if description is not UNSET:
            field_dict["description"] = description
        if reference is not UNSET:
            field_dict["reference"] = reference
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_transaction_fees import AirbnbTransactionFees
        from ..models.airbnb_transaction_payout import AirbnbTransactionPayout
        d = dict(src_dict)
        transaction_id = d.pop("transactionId")

        status = AirbnbTransactionStatus(d.pop("status"))




        type_ = d.pop("type")

        is_payout = d.pop("isPayout")

        fees = AirbnbTransactionFees.from_dict(d.pop("fees"))




        payout = AirbnbTransactionPayout.from_dict(d.pop("payout"))




        on_inactive_listing = d.pop("onInactiveListing")

        unavailable_fields = cast(list[str], d.pop("unavailableFields"))


        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


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


        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_listing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_name = _parse_listing_name(d.pop("listingName", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


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

        reservation_start_date = _parse_reservation_start_date(d.pop("reservationStartDate", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))


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


        airbnb_transaction = cls(
            transaction_id=transaction_id,
            status=status,
            type_=type_,
            is_payout=is_payout,
            fees=fees,
            payout=payout,
            on_inactive_listing=on_inactive_listing,
            unavailable_fields=unavailable_fields,
            account_id=account_id,
            account_name=account_name,
            date=date,
            currency=currency,
            amount=amount,
            gross_amount=gross_amount,
            confirmation_code=confirmation_code,
            reservation_id=reservation_id,
            listing_id=listing_id,
            listing_name=listing_name,
            guest_name=guest_name,
            nights=nights,
            reservation_start_date=reservation_start_date,
            description=description,
            reference=reference,
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
