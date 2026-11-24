from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_reservation_status import AirbnbReservationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbReservation")



@_attrs_define
class AirbnbReservation:
    """ An Airbnb reservation as returned by the channel API. Use `confirmationCode` to address it in Airbnb operations, and
    `reservationId` to open the same stay on `GET /v1/reservations/{id}`. The fields after `payoutCurrency` are the
    Airbnb record as stored (Airbnb's raw status, amounts as decimal strings, stay datetimes); they are kept for
    existing integrations.

        Attributes:
            id (str): This Airbnb record's id in Repull. Example: 307200.
            confirmation_code (None | str): Airbnb confirmation code. Example: HMABC12345.
            reservation_id (None | str): The same stay on the unified reservations API: `GET /v1/reservations/{id}`. Null
                only while that record is still being created. Example: 667929.
            listing_id (None | str): The Repull listing id (`GET /v1/listings/{id}`). Example: 42343.
            airbnb_listing_id (None | str): Airbnb's own listing id — the value `?listing_id=` takes. Example: 53866721.
            account_id (None | str): Which connected Airbnb account this row belongs to — the Airbnb host id, as a string
                (they exceed 2^53). The same value `?account_id=` accepts and `GET /v1/connect/airbnb` returns as
                `accounts[].externalAccountId`. Example: 1772489413932732258.
            account_name (None | str): Display name of that connected Airbnb account. Example: Seaside Stays.
            status (AirbnbReservationStatus): Normalised status. Airbnb's own value is in `airbnbStatus`. Example: accepted.
            check_in (datetime.date | None):  Example: 2026-12-05.
            check_out (datetime.date | None):  Example: 2026-12-08.
            guest_name (None | str):
            guest_count (int | None):
            total_price (float | None): What the guest paid, in `currency`. Example: 233.51.
            currency (None | str):  Example: USD.
            payout (float | None): What the host is expected to receive, in `payoutCurrency`. Example: 190.32.
            payout_currency (None | str):  Example: USD.
            listing_airbnb_id (None | str | Unset): Internal link id of the Airbnb listing. Use `airbnbListingId` or
                `listingId` instead.
            airbnb_reservation_id (None | str | Unset): Same as `confirmationCode`.
            host_id (None | str | Unset): Same as `accountId`.
            guest_airbnb_id (None | str | Unset): The guest's Airbnb user id.
            guest_first_name (None | str | Unset):
            guest_last_name (None | str | Unset):
            guest_profile_picture (None | str | Unset):
            airbnb_status (None | str | Unset): Airbnb's raw status: `accept`, `pending`, `cancelled_by_guest`,
                `cancelled_by_host`, `cancelled_by_admin`, `deny`, `failed_verification`, `pending_voided`, `checkpoint_voided`,
                `timeout`, … Example: accept.
            cancellation_policy (None | str | Unset):  Example: moderate.
            cancellation_reason (None | str | Unset):
            total_paid_amount (None | str | Unset): `totalPrice` as a decimal string. Example: 233.51.
            total_paid_currency (None | str | Unset):  Example: USD.
            expected_payout_amount (None | str | Unset): `payout` as a decimal string. Example: 190.32.
            expected_payout_currency (None | str | Unset):  Example: USD.
            canceled_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            check_in_datetime (datetime.datetime | None | Unset): Check-in date at 00:00 UTC. Prefer `checkIn`.
            check_out_datetime (datetime.datetime | None | Unset): Check-out date at 00:00 UTC. Prefer `checkOut`.
            time_zone (None | str | Unset):  Example: America/Costa_Rica.
            customer_id (None | str | Unset): Your workspace id.
            guest_id (None | str | Unset): The guest on `GET /v1/guests/{id}`.
     """

    id: str
    confirmation_code: None | str
    reservation_id: None | str
    listing_id: None | str
    airbnb_listing_id: None | str
    account_id: None | str
    account_name: None | str
    status: AirbnbReservationStatus
    check_in: datetime.date | None
    check_out: datetime.date | None
    guest_name: None | str
    guest_count: int | None
    total_price: float | None
    currency: None | str
    payout: float | None
    payout_currency: None | str
    listing_airbnb_id: None | str | Unset = UNSET
    airbnb_reservation_id: None | str | Unset = UNSET
    host_id: None | str | Unset = UNSET
    guest_airbnb_id: None | str | Unset = UNSET
    guest_first_name: None | str | Unset = UNSET
    guest_last_name: None | str | Unset = UNSET
    guest_profile_picture: None | str | Unset = UNSET
    airbnb_status: None | str | Unset = UNSET
    cancellation_policy: None | str | Unset = UNSET
    cancellation_reason: None | str | Unset = UNSET
    total_paid_amount: None | str | Unset = UNSET
    total_paid_currency: None | str | Unset = UNSET
    expected_payout_amount: None | str | Unset = UNSET
    expected_payout_currency: None | str | Unset = UNSET
    canceled_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    check_in_datetime: datetime.datetime | None | Unset = UNSET
    check_out_datetime: datetime.datetime | None | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    guest_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        confirmation_code: None | str
        confirmation_code = self.confirmation_code

        reservation_id: None | str
        reservation_id = self.reservation_id

        listing_id: None | str
        listing_id = self.listing_id

        airbnb_listing_id: None | str
        airbnb_listing_id = self.airbnb_listing_id

        account_id: None | str
        account_id = self.account_id

        account_name: None | str
        account_name = self.account_name

        status = self.status.value

        check_in: None | str
        if isinstance(self.check_in, datetime.date):
            check_in = self.check_in.isoformat()
        else:
            check_in = self.check_in

        check_out: None | str
        if isinstance(self.check_out, datetime.date):
            check_out = self.check_out.isoformat()
        else:
            check_out = self.check_out

        guest_name: None | str
        guest_name = self.guest_name

        guest_count: int | None
        guest_count = self.guest_count

        total_price: float | None
        total_price = self.total_price

        currency: None | str
        currency = self.currency

        payout: float | None
        payout = self.payout

        payout_currency: None | str
        payout_currency = self.payout_currency

        listing_airbnb_id: None | str | Unset
        if isinstance(self.listing_airbnb_id, Unset):
            listing_airbnb_id = UNSET
        else:
            listing_airbnb_id = self.listing_airbnb_id

        airbnb_reservation_id: None | str | Unset
        if isinstance(self.airbnb_reservation_id, Unset):
            airbnb_reservation_id = UNSET
        else:
            airbnb_reservation_id = self.airbnb_reservation_id

        host_id: None | str | Unset
        if isinstance(self.host_id, Unset):
            host_id = UNSET
        else:
            host_id = self.host_id

        guest_airbnb_id: None | str | Unset
        if isinstance(self.guest_airbnb_id, Unset):
            guest_airbnb_id = UNSET
        else:
            guest_airbnb_id = self.guest_airbnb_id

        guest_first_name: None | str | Unset
        if isinstance(self.guest_first_name, Unset):
            guest_first_name = UNSET
        else:
            guest_first_name = self.guest_first_name

        guest_last_name: None | str | Unset
        if isinstance(self.guest_last_name, Unset):
            guest_last_name = UNSET
        else:
            guest_last_name = self.guest_last_name

        guest_profile_picture: None | str | Unset
        if isinstance(self.guest_profile_picture, Unset):
            guest_profile_picture = UNSET
        else:
            guest_profile_picture = self.guest_profile_picture

        airbnb_status: None | str | Unset
        if isinstance(self.airbnb_status, Unset):
            airbnb_status = UNSET
        else:
            airbnb_status = self.airbnb_status

        cancellation_policy: None | str | Unset
        if isinstance(self.cancellation_policy, Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = self.cancellation_policy

        cancellation_reason: None | str | Unset
        if isinstance(self.cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = self.cancellation_reason

        total_paid_amount: None | str | Unset
        if isinstance(self.total_paid_amount, Unset):
            total_paid_amount = UNSET
        else:
            total_paid_amount = self.total_paid_amount

        total_paid_currency: None | str | Unset
        if isinstance(self.total_paid_currency, Unset):
            total_paid_currency = UNSET
        else:
            total_paid_currency = self.total_paid_currency

        expected_payout_amount: None | str | Unset
        if isinstance(self.expected_payout_amount, Unset):
            expected_payout_amount = UNSET
        else:
            expected_payout_amount = self.expected_payout_amount

        expected_payout_currency: None | str | Unset
        if isinstance(self.expected_payout_currency, Unset):
            expected_payout_currency = UNSET
        else:
            expected_payout_currency = self.expected_payout_currency

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        check_in_datetime: None | str | Unset
        if isinstance(self.check_in_datetime, Unset):
            check_in_datetime = UNSET
        elif isinstance(self.check_in_datetime, datetime.datetime):
            check_in_datetime = self.check_in_datetime.isoformat()
        else:
            check_in_datetime = self.check_in_datetime

        check_out_datetime: None | str | Unset
        if isinstance(self.check_out_datetime, Unset):
            check_out_datetime = UNSET
        elif isinstance(self.check_out_datetime, datetime.datetime):
            check_out_datetime = self.check_out_datetime.isoformat()
        else:
            check_out_datetime = self.check_out_datetime

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        guest_id: None | str | Unset
        if isinstance(self.guest_id, Unset):
            guest_id = UNSET
        else:
            guest_id = self.guest_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "confirmationCode": confirmation_code,
            "reservationId": reservation_id,
            "listingId": listing_id,
            "airbnbListingId": airbnb_listing_id,
            "accountId": account_id,
            "accountName": account_name,
            "status": status,
            "checkIn": check_in,
            "checkOut": check_out,
            "guestName": guest_name,
            "guestCount": guest_count,
            "totalPrice": total_price,
            "currency": currency,
            "payout": payout,
            "payoutCurrency": payout_currency,
        })
        if listing_airbnb_id is not UNSET:
            field_dict["listingAirbnbId"] = listing_airbnb_id
        if airbnb_reservation_id is not UNSET:
            field_dict["airbnbReservationId"] = airbnb_reservation_id
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if guest_airbnb_id is not UNSET:
            field_dict["guestAirbnbId"] = guest_airbnb_id
        if guest_first_name is not UNSET:
            field_dict["guestFirstName"] = guest_first_name
        if guest_last_name is not UNSET:
            field_dict["guestLastName"] = guest_last_name
        if guest_profile_picture is not UNSET:
            field_dict["guestProfilePicture"] = guest_profile_picture
        if airbnb_status is not UNSET:
            field_dict["airbnbStatus"] = airbnb_status
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if cancellation_reason is not UNSET:
            field_dict["cancellationReason"] = cancellation_reason
        if total_paid_amount is not UNSET:
            field_dict["totalPaidAmount"] = total_paid_amount
        if total_paid_currency is not UNSET:
            field_dict["totalPaidCurrency"] = total_paid_currency
        if expected_payout_amount is not UNSET:
            field_dict["expectedPayoutAmount"] = expected_payout_amount
        if expected_payout_currency is not UNSET:
            field_dict["expectedPayoutCurrency"] = expected_payout_currency
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if check_in_datetime is not UNSET:
            field_dict["checkInDatetime"] = check_in_datetime
        if check_out_datetime is not UNSET:
            field_dict["checkOutDatetime"] = check_out_datetime
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_confirmation_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmationCode"))


        def _parse_reservation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId"))


        def _parse_listing_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        listing_id = _parse_listing_id(d.pop("listingId"))


        def _parse_airbnb_listing_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        airbnb_listing_id = _parse_airbnb_listing_id(d.pop("airbnbListingId"))


        def _parse_account_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_id = _parse_account_id(d.pop("accountId"))


        def _parse_account_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_name = _parse_account_name(d.pop("accountName"))


        status = AirbnbReservationStatus(d.pop("status"))




        def _parse_check_in(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_type_0 = isoparse(data).date()



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        check_in = _parse_check_in(d.pop("checkIn"))


        def _parse_check_out(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_type_0 = isoparse(data).date()



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        check_out = _parse_check_out(d.pop("checkOut"))


        def _parse_guest_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        guest_name = _parse_guest_name(d.pop("guestName"))


        def _parse_guest_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        guest_count = _parse_guest_count(d.pop("guestCount"))


        def _parse_total_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        total_price = _parse_total_price(d.pop("totalPrice"))


        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))


        def _parse_payout(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        payout = _parse_payout(d.pop("payout"))


        def _parse_payout_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payout_currency = _parse_payout_currency(d.pop("payoutCurrency"))


        def _parse_listing_airbnb_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_airbnb_id = _parse_listing_airbnb_id(d.pop("listingAirbnbId", UNSET))


        def _parse_airbnb_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airbnb_reservation_id = _parse_airbnb_reservation_id(d.pop("airbnbReservationId", UNSET))


        def _parse_host_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_id = _parse_host_id(d.pop("hostId", UNSET))


        def _parse_guest_airbnb_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_airbnb_id = _parse_guest_airbnb_id(d.pop("guestAirbnbId", UNSET))


        def _parse_guest_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_first_name = _parse_guest_first_name(d.pop("guestFirstName", UNSET))


        def _parse_guest_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_last_name = _parse_guest_last_name(d.pop("guestLastName", UNSET))


        def _parse_guest_profile_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_profile_picture = _parse_guest_profile_picture(d.pop("guestProfilePicture", UNSET))


        def _parse_airbnb_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airbnb_status = _parse_airbnb_status(d.pop("airbnbStatus", UNSET))


        def _parse_cancellation_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_policy = _parse_cancellation_policy(d.pop("cancellationPolicy", UNSET))


        def _parse_cancellation_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_reason = _parse_cancellation_reason(d.pop("cancellationReason", UNSET))


        def _parse_total_paid_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_paid_amount = _parse_total_paid_amount(d.pop("totalPaidAmount", UNSET))


        def _parse_total_paid_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_paid_currency = _parse_total_paid_currency(d.pop("totalPaidCurrency", UNSET))


        def _parse_expected_payout_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_payout_amount = _parse_expected_payout_amount(d.pop("expectedPayoutAmount", UNSET))


        def _parse_expected_payout_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_payout_currency = _parse_expected_payout_currency(d.pop("expectedPayoutCurrency", UNSET))


        def _parse_canceled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                canceled_at_type_0 = isoparse(data)



                return canceled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_check_in_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_datetime_type_0 = isoparse(data)



                return check_in_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        check_in_datetime = _parse_check_in_datetime(d.pop("checkInDatetime", UNSET))


        def _parse_check_out_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_datetime_type_0 = isoparse(data)



                return check_out_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        check_out_datetime = _parse_check_out_datetime(d.pop("checkOutDatetime", UNSET))


        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customerId", UNSET))


        def _parse_guest_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_id = _parse_guest_id(d.pop("guestId", UNSET))


        airbnb_reservation = cls(
            id=id,
            confirmation_code=confirmation_code,
            reservation_id=reservation_id,
            listing_id=listing_id,
            airbnb_listing_id=airbnb_listing_id,
            account_id=account_id,
            account_name=account_name,
            status=status,
            check_in=check_in,
            check_out=check_out,
            guest_name=guest_name,
            guest_count=guest_count,
            total_price=total_price,
            currency=currency,
            payout=payout,
            payout_currency=payout_currency,
            listing_airbnb_id=listing_airbnb_id,
            airbnb_reservation_id=airbnb_reservation_id,
            host_id=host_id,
            guest_airbnb_id=guest_airbnb_id,
            guest_first_name=guest_first_name,
            guest_last_name=guest_last_name,
            guest_profile_picture=guest_profile_picture,
            airbnb_status=airbnb_status,
            cancellation_policy=cancellation_policy,
            cancellation_reason=cancellation_reason,
            total_paid_amount=total_paid_amount,
            total_paid_currency=total_paid_currency,
            expected_payout_amount=expected_payout_amount,
            expected_payout_currency=expected_payout_currency,
            canceled_at=canceled_at,
            created_at=created_at,
            updated_at=updated_at,
            check_in_datetime=check_in_datetime,
            check_out_datetime=check_out_datetime,
            time_zone=time_zone,
            customer_id=customer_id,
            guest_id=guest_id,
        )


        airbnb_reservation.additional_properties = d
        return airbnb_reservation

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
