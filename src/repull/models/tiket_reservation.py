from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_reservation_status import TiketReservationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="TiketReservation")



@_attrs_define
class TiketReservation:
    """ One booked room of a tiket.com reservation, as tiket.com delivered it.

        Attributes:
            reservation_id (None | str | Unset): The Repull reservation this room became (`GET /v1/reservations/{id}`).
                `null` while the room type is not mapped to a listing; mapping it records the booking.
            confirmation_code (str | Unset): `<tiketReservationId>` for the first room, `<tiketReservationId>-2`, `-3`, …
                for the others.
            tiket_reservation_id (str | Unset): tiket.com's id of the whole booking.
            previous_tiket_reservation_id (None | str | Unset): Set when this booking replaced an earlier one. tiket.com
                sends a date change as a cancellation plus a new booking; Repull applies it as a change to the original
                reservation.
            room_index (int | Unset): 1 for the first room of the booking.
            property_id (None | str | Unset): tiket.com Hotel ID.
            room_type_code (None | str | Unset):
            rate_plan_code (None | str | Unset):
            rate_plan_name (None | str | Unset):
            check_in (datetime.date | None | Unset):
            check_out (datetime.date | None | Unset):
            adults (int | Unset):
            children (int | Unset):
            infants (int | Unset):
            guest_name (None | str | Unset):
            guest_country (None | str | Unset):
            total_amount (float | None | Unset): What the guest paid for this room.
            net_amount (float | None | Unset): What tiket.com pays the property for this room.
            currency (None | str | Unset):  Example: IDR.
            payment_type (None | str | Unset): Payment type as tiket.com sent it.
            payment_method (None | str | Unset): How tiket.com pays the property: `Virtual Credit Card` or `Bank Transfer`.
                Card details are never returned by the API. Example: Bank Transfer.
            meal_plan_code (None | str | Unset):
            non_refundable (bool | None | Unset):
            cancellation_policy (None | str | Unset): Cancellation policy text as tiket.com sent it.
            special_requests (None | str | Unset):
            status (TiketReservationStatus | Unset):
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
     """

    reservation_id: None | str | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    tiket_reservation_id: str | Unset = UNSET
    previous_tiket_reservation_id: None | str | Unset = UNSET
    room_index: int | Unset = UNSET
    property_id: None | str | Unset = UNSET
    room_type_code: None | str | Unset = UNSET
    rate_plan_code: None | str | Unset = UNSET
    rate_plan_name: None | str | Unset = UNSET
    check_in: datetime.date | None | Unset = UNSET
    check_out: datetime.date | None | Unset = UNSET
    adults: int | Unset = UNSET
    children: int | Unset = UNSET
    infants: int | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    guest_country: None | str | Unset = UNSET
    total_amount: float | None | Unset = UNSET
    net_amount: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    payment_type: None | str | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    meal_plan_code: None | str | Unset = UNSET
    non_refundable: bool | None | Unset = UNSET
    cancellation_policy: None | str | Unset = UNSET
    special_requests: None | str | Unset = UNSET
    status: TiketReservationStatus | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        confirmation_code = self.confirmation_code

        tiket_reservation_id = self.tiket_reservation_id

        previous_tiket_reservation_id: None | str | Unset
        if isinstance(self.previous_tiket_reservation_id, Unset):
            previous_tiket_reservation_id = UNSET
        else:
            previous_tiket_reservation_id = self.previous_tiket_reservation_id

        room_index = self.room_index

        property_id: None | str | Unset
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        room_type_code: None | str | Unset
        if isinstance(self.room_type_code, Unset):
            room_type_code = UNSET
        else:
            room_type_code = self.room_type_code

        rate_plan_code: None | str | Unset
        if isinstance(self.rate_plan_code, Unset):
            rate_plan_code = UNSET
        else:
            rate_plan_code = self.rate_plan_code

        rate_plan_name: None | str | Unset
        if isinstance(self.rate_plan_name, Unset):
            rate_plan_name = UNSET
        else:
            rate_plan_name = self.rate_plan_name

        check_in: None | str | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        elif isinstance(self.check_in, datetime.date):
            check_in = self.check_in.isoformat()
        else:
            check_in = self.check_in

        check_out: None | str | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        elif isinstance(self.check_out, datetime.date):
            check_out = self.check_out.isoformat()
        else:
            check_out = self.check_out

        adults = self.adults

        children = self.children

        infants = self.infants

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        guest_country: None | str | Unset
        if isinstance(self.guest_country, Unset):
            guest_country = UNSET
        else:
            guest_country = self.guest_country

        total_amount: float | None | Unset
        if isinstance(self.total_amount, Unset):
            total_amount = UNSET
        else:
            total_amount = self.total_amount

        net_amount: float | None | Unset
        if isinstance(self.net_amount, Unset):
            net_amount = UNSET
        else:
            net_amount = self.net_amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        payment_type: None | str | Unset
        if isinstance(self.payment_type, Unset):
            payment_type = UNSET
        else:
            payment_type = self.payment_type

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        meal_plan_code: None | str | Unset
        if isinstance(self.meal_plan_code, Unset):
            meal_plan_code = UNSET
        else:
            meal_plan_code = self.meal_plan_code

        non_refundable: bool | None | Unset
        if isinstance(self.non_refundable, Unset):
            non_refundable = UNSET
        else:
            non_refundable = self.non_refundable

        cancellation_policy: None | str | Unset
        if isinstance(self.cancellation_policy, Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = self.cancellation_policy

        special_requests: None | str | Unset
        if isinstance(self.special_requests, Unset):
            special_requests = UNSET
        else:
            special_requests = self.special_requests

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if tiket_reservation_id is not UNSET:
            field_dict["tiketReservationId"] = tiket_reservation_id
        if previous_tiket_reservation_id is not UNSET:
            field_dict["previousTiketReservationId"] = previous_tiket_reservation_id
        if room_index is not UNSET:
            field_dict["roomIndex"] = room_index
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if room_type_code is not UNSET:
            field_dict["roomTypeCode"] = room_type_code
        if rate_plan_code is not UNSET:
            field_dict["ratePlanCode"] = rate_plan_code
        if rate_plan_name is not UNSET:
            field_dict["ratePlanName"] = rate_plan_name
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if infants is not UNSET:
            field_dict["infants"] = infants
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if guest_country is not UNSET:
            field_dict["guestCountry"] = guest_country
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_type is not UNSET:
            field_dict["paymentType"] = payment_type
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if meal_plan_code is not UNSET:
            field_dict["mealPlanCode"] = meal_plan_code
        if non_refundable is not UNSET:
            field_dict["nonRefundable"] = non_refundable
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if special_requests is not UNSET:
            field_dict["specialRequests"] = special_requests
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        confirmation_code = d.pop("confirmationCode", UNSET)

        tiket_reservation_id = d.pop("tiketReservationId", UNSET)

        def _parse_previous_tiket_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_tiket_reservation_id = _parse_previous_tiket_reservation_id(d.pop("previousTiketReservationId", UNSET))


        room_index = d.pop("roomIndex", UNSET)

        def _parse_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))


        def _parse_room_type_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_type_code = _parse_room_type_code(d.pop("roomTypeCode", UNSET))


        def _parse_rate_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_plan_code = _parse_rate_plan_code(d.pop("ratePlanCode", UNSET))


        def _parse_rate_plan_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_plan_name = _parse_rate_plan_name(d.pop("ratePlanName", UNSET))


        def _parse_check_in(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_type_0 = isoparse(data).date()



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_type_0 = isoparse(data).date()



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        infants = d.pop("infants", UNSET)

        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        def _parse_guest_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_country = _parse_guest_country(d.pop("guestCountry", UNSET))


        def _parse_total_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_amount = _parse_total_amount(d.pop("totalAmount", UNSET))


        def _parse_net_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        net_amount = _parse_net_amount(d.pop("netAmount", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_payment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_type = _parse_payment_type(d.pop("paymentType", UNSET))


        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        def _parse_meal_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meal_plan_code = _parse_meal_plan_code(d.pop("mealPlanCode", UNSET))


        def _parse_non_refundable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        non_refundable = _parse_non_refundable(d.pop("nonRefundable", UNSET))


        def _parse_cancellation_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_policy = _parse_cancellation_policy(d.pop("cancellationPolicy", UNSET))


        def _parse_special_requests(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        special_requests = _parse_special_requests(d.pop("specialRequests", UNSET))


        _status = d.pop("status", UNSET)
        status: TiketReservationStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = TiketReservationStatus(_status)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        tiket_reservation = cls(
            reservation_id=reservation_id,
            confirmation_code=confirmation_code,
            tiket_reservation_id=tiket_reservation_id,
            previous_tiket_reservation_id=previous_tiket_reservation_id,
            room_index=room_index,
            property_id=property_id,
            room_type_code=room_type_code,
            rate_plan_code=rate_plan_code,
            rate_plan_name=rate_plan_name,
            check_in=check_in,
            check_out=check_out,
            adults=adults,
            children=children,
            infants=infants,
            guest_name=guest_name,
            guest_country=guest_country,
            total_amount=total_amount,
            net_amount=net_amount,
            currency=currency,
            payment_type=payment_type,
            payment_method=payment_method,
            meal_plan_code=meal_plan_code,
            non_refundable=non_refundable,
            cancellation_policy=cancellation_policy,
            special_requests=special_requests,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )


        tiket_reservation.additional_properties = d
        return tiket_reservation

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
