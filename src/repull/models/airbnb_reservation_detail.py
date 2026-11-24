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
  from ..models.airbnb_reservation import AirbnbReservation
  from ..models.airbnb_reservation_detail_custom_fields_type_0 import AirbnbReservationDetailCustomFieldsType0
  from ..models.airbnb_reservation_detail_guest_details_type_0 import AirbnbReservationDetailGuestDetailsType0
  from ..models.airbnb_reservation_detail_price_breakdown_type_0 import AirbnbReservationDetailPriceBreakdownType0





T = TypeVar("T", bound="AirbnbReservationDetail")



@_attrs_define
class AirbnbReservationDetail:
    """ One Airbnb reservation: the unified reservation (the same record as `GET /v1/reservations/{reservationId}`, as
    stored), the connected account and payout, and `airbnb` — the row `GET /v1/channels/airbnb/reservations` returns for
    it.

        Attributes:
            id (str): The unified reservation id (same as `reservationId`). Example: 667929.
            reservation_id (str): The unified reservation id: `GET /v1/reservations/{id}`. Example: 667929.
            confirmation_code (str):  Example: HMAS8FEPJM.
            listing_id (str): The Repull listing id. Example: 42343.
            airbnb_listing_id (None | str): Airbnb's own listing id.
            account_id (None | str): The connected Airbnb account (host id, as a string).
            account_name (None | str):
            status (str): Airbnb's status as stored on the reservation (`accept`, `cancelled`, `decline`, `pending_voided`,
                …). The normalised value is `airbnb.status`. Example: accept.
            check_in (datetime.date):
            check_out (datetime.date):
            guest_name (None | str):
            guest_count (int | None):
            total_price (None | str): Total as a decimal string, in `currency`. Example: 245.03.
            currency (None | str):  Example: EUR.
            payout (float | None): What the host is expected to receive, in `payoutCurrency`.
            payout_currency (None | str):
            airbnb (AirbnbReservation | None): The Airbnb record, in the list endpoint's shape. Null only while it is still
                being imported.
            guest_id (None | str | Unset):
            platform (None | str | Unset):  Example: airbnb.
            pms_source (None | str | Unset):
            booking_reservation_number (None | str | Unset):
            unit_external_id (None | str | Unset):
            unit_name (None | str | Unset):
            payment_status (None | str | Unset):  Example: paid.
            guest_details (AirbnbReservationDetailGuestDetailsType0 | None | Unset): Guest counts: `numberOfGuests`,
                `numberOfAdults`, `numberOfChildren`, `numberOfInfants`, `numberOfPets`.
            price_breakdown (AirbnbReservationDetailPriceBreakdownType0 | None | Unset): Nightly rates, fees, taxes,
                discounts, `hostPayout`.
            custom_fields (AirbnbReservationDetailCustomFieldsType0 | None | Unset):
            cancellation_policy (None | str | Unset):
            cancellation_reason (None | str | Unset):
            cancellation_date (datetime.datetime | None | Unset):
            host_notes (None | str | Unset):
            guest_notes (None | str | Unset):
            internal_notes (None | str | Unset):
            time_zone (None | str | Unset):
            check_in_time (None | str | Unset):
            check_out_time (None | str | Unset):
            customer_id (None | str | Unset):
            airbnb_host_id (None | str | Unset): Use `accountId`.
            booked_at (datetime.datetime | None | Unset):
     """

    id: str
    reservation_id: str
    confirmation_code: str
    listing_id: str
    airbnb_listing_id: None | str
    account_id: None | str
    account_name: None | str
    status: str
    check_in: datetime.date
    check_out: datetime.date
    guest_name: None | str
    guest_count: int | None
    total_price: None | str
    currency: None | str
    payout: float | None
    payout_currency: None | str
    airbnb: AirbnbReservation | None
    guest_id: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    pms_source: None | str | Unset = UNSET
    booking_reservation_number: None | str | Unset = UNSET
    unit_external_id: None | str | Unset = UNSET
    unit_name: None | str | Unset = UNSET
    payment_status: None | str | Unset = UNSET
    guest_details: AirbnbReservationDetailGuestDetailsType0 | None | Unset = UNSET
    price_breakdown: AirbnbReservationDetailPriceBreakdownType0 | None | Unset = UNSET
    custom_fields: AirbnbReservationDetailCustomFieldsType0 | None | Unset = UNSET
    cancellation_policy: None | str | Unset = UNSET
    cancellation_reason: None | str | Unset = UNSET
    cancellation_date: datetime.datetime | None | Unset = UNSET
    host_notes: None | str | Unset = UNSET
    guest_notes: None | str | Unset = UNSET
    internal_notes: None | str | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    airbnb_host_id: None | str | Unset = UNSET
    booked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_reservation import AirbnbReservation
        from ..models.airbnb_reservation_detail_custom_fields_type_0 import AirbnbReservationDetailCustomFieldsType0
        from ..models.airbnb_reservation_detail_guest_details_type_0 import AirbnbReservationDetailGuestDetailsType0
        from ..models.airbnb_reservation_detail_price_breakdown_type_0 import AirbnbReservationDetailPriceBreakdownType0
        id = self.id

        reservation_id = self.reservation_id

        confirmation_code = self.confirmation_code

        listing_id = self.listing_id

        airbnb_listing_id: None | str
        airbnb_listing_id = self.airbnb_listing_id

        account_id: None | str
        account_id = self.account_id

        account_name: None | str
        account_name = self.account_name

        status = self.status

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        guest_name: None | str
        guest_name = self.guest_name

        guest_count: int | None
        guest_count = self.guest_count

        total_price: None | str
        total_price = self.total_price

        currency: None | str
        currency = self.currency

        payout: float | None
        payout = self.payout

        payout_currency: None | str
        payout_currency = self.payout_currency

        airbnb: dict[str, Any] | None
        if isinstance(self.airbnb, AirbnbReservation):
            airbnb = self.airbnb.to_dict()
        else:
            airbnb = self.airbnb

        guest_id: None | str | Unset
        if isinstance(self.guest_id, Unset):
            guest_id = UNSET
        else:
            guest_id = self.guest_id

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        pms_source: None | str | Unset
        if isinstance(self.pms_source, Unset):
            pms_source = UNSET
        else:
            pms_source = self.pms_source

        booking_reservation_number: None | str | Unset
        if isinstance(self.booking_reservation_number, Unset):
            booking_reservation_number = UNSET
        else:
            booking_reservation_number = self.booking_reservation_number

        unit_external_id: None | str | Unset
        if isinstance(self.unit_external_id, Unset):
            unit_external_id = UNSET
        else:
            unit_external_id = self.unit_external_id

        unit_name: None | str | Unset
        if isinstance(self.unit_name, Unset):
            unit_name = UNSET
        else:
            unit_name = self.unit_name

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = self.payment_status

        guest_details: dict[str, Any] | None | Unset
        if isinstance(self.guest_details, Unset):
            guest_details = UNSET
        elif isinstance(self.guest_details, AirbnbReservationDetailGuestDetailsType0):
            guest_details = self.guest_details.to_dict()
        else:
            guest_details = self.guest_details

        price_breakdown: dict[str, Any] | None | Unset
        if isinstance(self.price_breakdown, Unset):
            price_breakdown = UNSET
        elif isinstance(self.price_breakdown, AirbnbReservationDetailPriceBreakdownType0):
            price_breakdown = self.price_breakdown.to_dict()
        else:
            price_breakdown = self.price_breakdown

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, AirbnbReservationDetailCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

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

        cancellation_date: None | str | Unset
        if isinstance(self.cancellation_date, Unset):
            cancellation_date = UNSET
        elif isinstance(self.cancellation_date, datetime.datetime):
            cancellation_date = self.cancellation_date.isoformat()
        else:
            cancellation_date = self.cancellation_date

        host_notes: None | str | Unset
        if isinstance(self.host_notes, Unset):
            host_notes = UNSET
        else:
            host_notes = self.host_notes

        guest_notes: None | str | Unset
        if isinstance(self.guest_notes, Unset):
            guest_notes = UNSET
        else:
            guest_notes = self.guest_notes

        internal_notes: None | str | Unset
        if isinstance(self.internal_notes, Unset):
            internal_notes = UNSET
        else:
            internal_notes = self.internal_notes

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        airbnb_host_id: None | str | Unset
        if isinstance(self.airbnb_host_id, Unset):
            airbnb_host_id = UNSET
        else:
            airbnb_host_id = self.airbnb_host_id

        booked_at: None | str | Unset
        if isinstance(self.booked_at, Unset):
            booked_at = UNSET
        elif isinstance(self.booked_at, datetime.datetime):
            booked_at = self.booked_at.isoformat()
        else:
            booked_at = self.booked_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "reservationId": reservation_id,
            "confirmationCode": confirmation_code,
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
            "airbnb": airbnb,
        })
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if pms_source is not UNSET:
            field_dict["pmsSource"] = pms_source
        if booking_reservation_number is not UNSET:
            field_dict["bookingReservationNumber"] = booking_reservation_number
        if unit_external_id is not UNSET:
            field_dict["unitExternalId"] = unit_external_id
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if guest_details is not UNSET:
            field_dict["guestDetails"] = guest_details
        if price_breakdown is not UNSET:
            field_dict["priceBreakdown"] = price_breakdown
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if cancellation_reason is not UNSET:
            field_dict["cancellationReason"] = cancellation_reason
        if cancellation_date is not UNSET:
            field_dict["cancellationDate"] = cancellation_date
        if host_notes is not UNSET:
            field_dict["hostNotes"] = host_notes
        if guest_notes is not UNSET:
            field_dict["guestNotes"] = guest_notes
        if internal_notes is not UNSET:
            field_dict["internalNotes"] = internal_notes
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if airbnb_host_id is not UNSET:
            field_dict["airbnbHostId"] = airbnb_host_id
        if booked_at is not UNSET:
            field_dict["bookedAt"] = booked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_reservation import AirbnbReservation
        from ..models.airbnb_reservation_detail_custom_fields_type_0 import AirbnbReservationDetailCustomFieldsType0
        from ..models.airbnb_reservation_detail_guest_details_type_0 import AirbnbReservationDetailGuestDetailsType0
        from ..models.airbnb_reservation_detail_price_breakdown_type_0 import AirbnbReservationDetailPriceBreakdownType0
        d = dict(src_dict)
        id = d.pop("id")

        reservation_id = d.pop("reservationId")

        confirmation_code = d.pop("confirmationCode")

        listing_id = d.pop("listingId")

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


        status = d.pop("status")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




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


        def _parse_total_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

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


        def _parse_airbnb(data: object) -> AirbnbReservation | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                airbnb_type_1 = AirbnbReservation.from_dict(data)



                return airbnb_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbReservation | None, data)

        airbnb = _parse_airbnb(d.pop("airbnb"))


        def _parse_guest_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_id = _parse_guest_id(d.pop("guestId", UNSET))


        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))


        def _parse_pms_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pms_source = _parse_pms_source(d.pop("pmsSource", UNSET))


        def _parse_booking_reservation_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_reservation_number = _parse_booking_reservation_number(d.pop("bookingReservationNumber", UNSET))


        def _parse_unit_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_external_id = _parse_unit_external_id(d.pop("unitExternalId", UNSET))


        def _parse_unit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_name = _parse_unit_name(d.pop("unitName", UNSET))


        def _parse_payment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))


        def _parse_guest_details(data: object) -> AirbnbReservationDetailGuestDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guest_details_type_0 = AirbnbReservationDetailGuestDetailsType0.from_dict(data)



                return guest_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbReservationDetailGuestDetailsType0 | None | Unset, data)

        guest_details = _parse_guest_details(d.pop("guestDetails", UNSET))


        def _parse_price_breakdown(data: object) -> AirbnbReservationDetailPriceBreakdownType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_breakdown_type_0 = AirbnbReservationDetailPriceBreakdownType0.from_dict(data)



                return price_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbReservationDetailPriceBreakdownType0 | None | Unset, data)

        price_breakdown = _parse_price_breakdown(d.pop("priceBreakdown", UNSET))


        def _parse_custom_fields(data: object) -> AirbnbReservationDetailCustomFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = AirbnbReservationDetailCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbReservationDetailCustomFieldsType0 | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


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


        def _parse_cancellation_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancellation_date_type_0 = isoparse(data)



                return cancellation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cancellation_date = _parse_cancellation_date(d.pop("cancellationDate", UNSET))


        def _parse_host_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_notes = _parse_host_notes(d.pop("hostNotes", UNSET))


        def _parse_guest_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_notes = _parse_guest_notes(d.pop("guestNotes", UNSET))


        def _parse_internal_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_notes = _parse_internal_notes(d.pop("internalNotes", UNSET))


        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))


        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))


        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customerId", UNSET))


        def _parse_airbnb_host_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airbnb_host_id = _parse_airbnb_host_id(d.pop("airbnbHostId", UNSET))


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

        booked_at = _parse_booked_at(d.pop("bookedAt", UNSET))


        airbnb_reservation_detail = cls(
            id=id,
            reservation_id=reservation_id,
            confirmation_code=confirmation_code,
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
            airbnb=airbnb,
            guest_id=guest_id,
            platform=platform,
            pms_source=pms_source,
            booking_reservation_number=booking_reservation_number,
            unit_external_id=unit_external_id,
            unit_name=unit_name,
            payment_status=payment_status,
            guest_details=guest_details,
            price_breakdown=price_breakdown,
            custom_fields=custom_fields,
            cancellation_policy=cancellation_policy,
            cancellation_reason=cancellation_reason,
            cancellation_date=cancellation_date,
            host_notes=host_notes,
            guest_notes=guest_notes,
            internal_notes=internal_notes,
            time_zone=time_zone,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            customer_id=customer_id,
            airbnb_host_id=airbnb_host_id,
            booked_at=booked_at,
        )


        airbnb_reservation_detail.additional_properties = d
        return airbnb_reservation_detail

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
