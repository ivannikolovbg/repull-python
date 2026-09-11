from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_reservation_room_status import BookingReservationRoomStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingReservationRoom")



@_attrs_define
class BookingReservationRoom:
    """ A single reserved room within a Booking.com reservation. Raw Booking OTA shape — passed through unmodified from the
    connector.

        Attributes:
            id (str | Unset): Room id.
            roomreservation_id (str | Unset): Per-room reservation id.
            arrival_date (str | Unset): Room arrival date (YYYY-MM-DD).
            departure_date (str | Unset): Room departure date (YYYY-MM-DD).
            guest_name (None | str | Unset):
            numberofguests (int | None | Unset):
            adults (int | None | Unset):
            children (int | None | Unset):
            meal_plan (None | str | Unset):
            totalprice (float | None | Unset):
            currencycode (None | str | Unset):
            status (BookingReservationRoomStatus | Unset):
            special_requests (list[str] | None | Unset):
     """

    id: str | Unset = UNSET
    roomreservation_id: str | Unset = UNSET
    arrival_date: str | Unset = UNSET
    departure_date: str | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    numberofguests: int | None | Unset = UNSET
    adults: int | None | Unset = UNSET
    children: int | None | Unset = UNSET
    meal_plan: None | str | Unset = UNSET
    totalprice: float | None | Unset = UNSET
    currencycode: None | str | Unset = UNSET
    status: BookingReservationRoomStatus | Unset = UNSET
    special_requests: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        roomreservation_id = self.roomreservation_id

        arrival_date = self.arrival_date

        departure_date = self.departure_date

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        numberofguests: int | None | Unset
        if isinstance(self.numberofguests, Unset):
            numberofguests = UNSET
        else:
            numberofguests = self.numberofguests

        adults: int | None | Unset
        if isinstance(self.adults, Unset):
            adults = UNSET
        else:
            adults = self.adults

        children: int | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        else:
            children = self.children

        meal_plan: None | str | Unset
        if isinstance(self.meal_plan, Unset):
            meal_plan = UNSET
        else:
            meal_plan = self.meal_plan

        totalprice: float | None | Unset
        if isinstance(self.totalprice, Unset):
            totalprice = UNSET
        else:
            totalprice = self.totalprice

        currencycode: None | str | Unset
        if isinstance(self.currencycode, Unset):
            currencycode = UNSET
        else:
            currencycode = self.currencycode

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        special_requests: list[str] | None | Unset
        if isinstance(self.special_requests, Unset):
            special_requests = UNSET
        elif isinstance(self.special_requests, list):
            special_requests = self.special_requests


        else:
            special_requests = self.special_requests


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if roomreservation_id is not UNSET:
            field_dict["roomreservation_id"] = roomreservation_id
        if arrival_date is not UNSET:
            field_dict["arrival_date"] = arrival_date
        if departure_date is not UNSET:
            field_dict["departure_date"] = departure_date
        if guest_name is not UNSET:
            field_dict["guest_name"] = guest_name
        if numberofguests is not UNSET:
            field_dict["numberofguests"] = numberofguests
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if meal_plan is not UNSET:
            field_dict["meal_plan"] = meal_plan
        if totalprice is not UNSET:
            field_dict["totalprice"] = totalprice
        if currencycode is not UNSET:
            field_dict["currencycode"] = currencycode
        if status is not UNSET:
            field_dict["status"] = status
        if special_requests is not UNSET:
            field_dict["special_requests"] = special_requests

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        roomreservation_id = d.pop("roomreservation_id", UNSET)

        arrival_date = d.pop("arrival_date", UNSET)

        departure_date = d.pop("departure_date", UNSET)

        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guest_name", UNSET))


        def _parse_numberofguests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        numberofguests = _parse_numberofguests(d.pop("numberofguests", UNSET))


        def _parse_adults(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adults = _parse_adults(d.pop("adults", UNSET))


        def _parse_children(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))


        def _parse_meal_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meal_plan = _parse_meal_plan(d.pop("meal_plan", UNSET))


        def _parse_totalprice(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        totalprice = _parse_totalprice(d.pop("totalprice", UNSET))


        def _parse_currencycode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currencycode = _parse_currencycode(d.pop("currencycode", UNSET))


        _status = d.pop("status", UNSET)
        status: BookingReservationRoomStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BookingReservationRoomStatus(_status)




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


        booking_reservation_room = cls(
            id=id,
            roomreservation_id=roomreservation_id,
            arrival_date=arrival_date,
            departure_date=departure_date,
            guest_name=guest_name,
            numberofguests=numberofguests,
            adults=adults,
            children=children,
            meal_plan=meal_plan,
            totalprice=totalprice,
            currencycode=currencycode,
            status=status,
            special_requests=special_requests,
        )


        booking_reservation_room.additional_properties = d
        return booking_reservation_room

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
