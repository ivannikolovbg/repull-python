from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_reservation_payment_status import BookingReservationPaymentStatus
from ..models.booking_reservation_status import BookingReservationStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_reservation_customer import BookingReservationCustomer
  from ..models.booking_reservation_room import BookingReservationRoom





T = TypeVar("T", bound="BookingReservation")



@_attrs_define
class BookingReservation:
    """ A Booking.com reservation as returned by `GET /v1/channels/booking/reservations`.

    **This is the RAW Booking.com OTA payload**, passed through from the connector unmodified — it is NOT renormalised
    to the unified Repull reservation shape (`GET /v1/reservations`). Field names, casing, and nesting follow Booking's
    OTA format (nested `room[]`, `customer`, snake_case keys). Additional Booking-side fields not enumerated here may be
    present, and any field may be absent depending on the reservation `type` (`new` / `modified` / `details`). For a
    channel-agnostic, stable reservation contract, use `GET /v1/reservations` instead.

        Attributes:
            id (str | Unset): Booking.com reservation id.
            status (BookingReservationStatus | Unset):
            date (None | str | Unset): Booking date (YYYY-MM-DD).
            time (None | str | Unset): Booking time.
            customer (BookingReservationCustomer | Unset): Guest / customer block (name, contact, address) in Booking's OTA
                shape.
            room (list[BookingReservationRoom] | Unset): Reserved rooms.
            total_price (float | None | Unset):
            currency_code (None | str | Unset):
            payment_status (BookingReservationPaymentStatus | Unset):
            commission_amount (float | None | Unset):
            cancellation_deadline (None | str | Unset):
            special_requests (list[str] | None | Unset):
            company_name (None | str | Unset):
     """

    id: str | Unset = UNSET
    status: BookingReservationStatus | Unset = UNSET
    date: None | str | Unset = UNSET
    time: None | str | Unset = UNSET
    customer: BookingReservationCustomer | Unset = UNSET
    room: list[BookingReservationRoom] | Unset = UNSET
    total_price: float | None | Unset = UNSET
    currency_code: None | str | Unset = UNSET
    payment_status: BookingReservationPaymentStatus | Unset = UNSET
    commission_amount: float | None | Unset = UNSET
    cancellation_deadline: None | str | Unset = UNSET
    special_requests: list[str] | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_reservation_customer import BookingReservationCustomer
        from ..models.booking_reservation_room import BookingReservationRoom
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        customer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        room: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.room, Unset):
            room = []
            for room_item_data in self.room:
                room_item = room_item_data.to_dict()
                room.append(room_item)



        total_price: float | None | Unset
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value


        commission_amount: float | None | Unset
        if isinstance(self.commission_amount, Unset):
            commission_amount = UNSET
        else:
            commission_amount = self.commission_amount

        cancellation_deadline: None | str | Unset
        if isinstance(self.cancellation_deadline, Unset):
            cancellation_deadline = UNSET
        else:
            cancellation_deadline = self.cancellation_deadline

        special_requests: list[str] | None | Unset
        if isinstance(self.special_requests, Unset):
            special_requests = UNSET
        elif isinstance(self.special_requests, list):
            special_requests = self.special_requests


        else:
            special_requests = self.special_requests

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if date is not UNSET:
            field_dict["date"] = date
        if time is not UNSET:
            field_dict["time"] = time
        if customer is not UNSET:
            field_dict["customer"] = customer
        if room is not UNSET:
            field_dict["room"] = room
        if total_price is not UNSET:
            field_dict["total_price"] = total_price
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if commission_amount is not UNSET:
            field_dict["commission_amount"] = commission_amount
        if cancellation_deadline is not UNSET:
            field_dict["cancellation_deadline"] = cancellation_deadline
        if special_requests is not UNSET:
            field_dict["special_requests"] = special_requests
        if company_name is not UNSET:
            field_dict["company_name"] = company_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_reservation_customer import BookingReservationCustomer
        from ..models.booking_reservation_room import BookingReservationRoom
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: BookingReservationStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BookingReservationStatus(_status)




        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time = _parse_time(d.pop("time", UNSET))


        _customer = d.pop("customer", UNSET)
        customer: BookingReservationCustomer | Unset
        if isinstance(_customer,  Unset):
            customer = UNSET
        else:
            customer = BookingReservationCustomer.from_dict(_customer)




        _room = d.pop("room", UNSET)
        room: list[BookingReservationRoom] | Unset = UNSET
        if _room is not UNSET:
            room = []
            for room_item_data in _room:
                room_item = BookingReservationRoom.from_dict(room_item_data)



                room.append(room_item)


        def _parse_total_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_price = _parse_total_price(d.pop("total_price", UNSET))


        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currency_code", UNSET))


        _payment_status = d.pop("payment_status", UNSET)
        payment_status: BookingReservationPaymentStatus | Unset
        if isinstance(_payment_status,  Unset):
            payment_status = UNSET
        else:
            payment_status = BookingReservationPaymentStatus(_payment_status)




        def _parse_commission_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        commission_amount = _parse_commission_amount(d.pop("commission_amount", UNSET))


        def _parse_cancellation_deadline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_deadline = _parse_cancellation_deadline(d.pop("cancellation_deadline", UNSET))


        def _parse_special_requests(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                special_requests_type_0 = cast(list[str], data)

                return special_requests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        special_requests = _parse_special_requests(d.pop("special_requests", UNSET))


        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))


        booking_reservation = cls(
            id=id,
            status=status,
            date=date,
            time=time,
            customer=customer,
            room=room,
            total_price=total_price,
            currency_code=currency_code,
            payment_status=payment_status,
            commission_amount=commission_amount,
            cancellation_deadline=cancellation_deadline,
            special_requests=special_requests,
            company_name=company_name,
        )


        booking_reservation.additional_properties = d
        return booking_reservation

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
