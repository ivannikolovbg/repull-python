from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_vrbo_transactions_response_200_data_item_status import ListVrboTransactionsResponse200DataItemStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.list_vrbo_transactions_response_200_data_item_payout import ListVrboTransactionsResponse200DataItemPayout





T = TypeVar("T", bound="ListVrboTransactionsResponse200DataItem")



@_attrs_define
class ListVrboTransactionsResponse200DataItem:
    """ 
        Attributes:
            transaction_id (str | Unset): Stable: the deposit's reference number on a Payout row;
                `<reference>:<confirmationCode>:<n>` on a line; `upcoming:<confirmationCode>:<n>` on a scheduled payout.
            account_id (None | str | Unset):
            account_name (None | str | Unset):
            status (ListVrboTransactionsResponse200DataItemStatus | Unset):
            type_ (str | Unset): `Payout` (the bank deposit), `Reservation` (a booking it paid), `Adjustment` (money taken
                back from it). Example: Reservation.
            is_payout (bool | Unset):
            date (datetime.date | None | Unset):
            currency (None | str | Unset):
            amount (float | None | Unset): Signed: what this line adds to its deposit. On a Payout row, the amount
                deposited.
            payout (ListVrboTransactionsResponse200DataItemPayout | Unset):
            confirmation_code (None | str | Unset):
            reservation_id (int | None | Unset): The Repull reservation, when the booking is in the workspace.
            listing_id (int | None | Unset):
            vrbo_listing_number (None | str | Unset):
            on_inactive_listing (bool | Unset):
            guest_name (None | str | Unset):
            upcoming_status (None | str | Unset): On an UPCOMING line: Vrbo's status for the payout (`Scheduled`, `Blocked`,
                …).
            unavailable_fields (list[str] | Unset):
            synced_at (None | str | Unset):
     """

    transaction_id: str | Unset = UNSET
    account_id: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    status: ListVrboTransactionsResponse200DataItemStatus | Unset = UNSET
    type_: str | Unset = UNSET
    is_payout: bool | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    amount: float | None | Unset = UNSET
    payout: ListVrboTransactionsResponse200DataItemPayout | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    listing_id: int | None | Unset = UNSET
    vrbo_listing_number: None | str | Unset = UNSET
    on_inactive_listing: bool | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    upcoming_status: None | str | Unset = UNSET
    unavailable_fields: list[str] | Unset = UNSET
    synced_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_vrbo_transactions_response_200_data_item_payout import ListVrboTransactionsResponse200DataItemPayout
        transaction_id = self.transaction_id

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        type_ = self.type_

        is_payout = self.is_payout

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

        payout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payout, Unset):
            payout = self.payout.to_dict()

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

        vrbo_listing_number: None | str | Unset
        if isinstance(self.vrbo_listing_number, Unset):
            vrbo_listing_number = UNSET
        else:
            vrbo_listing_number = self.vrbo_listing_number

        on_inactive_listing = self.on_inactive_listing

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        upcoming_status: None | str | Unset
        if isinstance(self.upcoming_status, Unset):
            upcoming_status = UNSET
        else:
            upcoming_status = self.upcoming_status

        unavailable_fields: list[str] | Unset = UNSET
        if not isinstance(self.unavailable_fields, Unset):
            unavailable_fields = self.unavailable_fields



        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        else:
            synced_at = self.synced_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_payout is not UNSET:
            field_dict["isPayout"] = is_payout
        if date is not UNSET:
            field_dict["date"] = date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payout is not UNSET:
            field_dict["payout"] = payout
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number
        if on_inactive_listing is not UNSET:
            field_dict["onInactiveListing"] = on_inactive_listing
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if upcoming_status is not UNSET:
            field_dict["upcomingStatus"] = upcoming_status
        if unavailable_fields is not UNSET:
            field_dict["unavailableFields"] = unavailable_fields
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_vrbo_transactions_response_200_data_item_payout import ListVrboTransactionsResponse200DataItemPayout
        d = dict(src_dict)
        transaction_id = d.pop("transactionId", UNSET)

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


        _status = d.pop("status", UNSET)
        status: ListVrboTransactionsResponse200DataItemStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ListVrboTransactionsResponse200DataItemStatus(_status)




        type_ = d.pop("type", UNSET)

        is_payout = d.pop("isPayout", UNSET)

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


        _payout = d.pop("payout", UNSET)
        payout: ListVrboTransactionsResponse200DataItemPayout | Unset
        if isinstance(_payout,  Unset):
            payout = UNSET
        else:
            payout = ListVrboTransactionsResponse200DataItemPayout.from_dict(_payout)




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


        def _parse_vrbo_listing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vrbo_listing_number = _parse_vrbo_listing_number(d.pop("vrboListingNumber", UNSET))


        on_inactive_listing = d.pop("onInactiveListing", UNSET)

        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        def _parse_upcoming_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upcoming_status = _parse_upcoming_status(d.pop("upcomingStatus", UNSET))


        unavailable_fields = cast(list[str], d.pop("unavailableFields", UNSET))


        def _parse_synced_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        synced_at = _parse_synced_at(d.pop("syncedAt", UNSET))


        list_vrbo_transactions_response_200_data_item = cls(
            transaction_id=transaction_id,
            account_id=account_id,
            account_name=account_name,
            status=status,
            type_=type_,
            is_payout=is_payout,
            date=date,
            currency=currency,
            amount=amount,
            payout=payout,
            confirmation_code=confirmation_code,
            reservation_id=reservation_id,
            listing_id=listing_id,
            vrbo_listing_number=vrbo_listing_number,
            on_inactive_listing=on_inactive_listing,
            guest_name=guest_name,
            upcoming_status=upcoming_status,
            unavailable_fields=unavailable_fields,
            synced_at=synced_at,
        )


        list_vrbo_transactions_response_200_data_item.additional_properties = d
        return list_vrbo_transactions_response_200_data_item

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
