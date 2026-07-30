from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_availability_update_status import BookingAvailabilityUpdateStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_availability_update_date_range import BookingAvailabilityUpdateDateRange
  from ..models.booking_pricing_rate_update_restrictions import BookingPricingRateUpdateRestrictions





T = TypeVar("T", bound="BookingAvailabilityUpdate")



@_attrs_define
class BookingAvailabilityUpdate:
    """ One (room, rate-plan, date-range) availability update. Carries inventory (`availableRooms`), the dedicated stop-sell
    flag (`closed`), and the same length-of-stay / arrival restrictions as a rate update.

        Attributes:
            room_id (str): Booking.com room id.
            rate_id (str): Booking.com rate-plan id.
            date_range (BookingAvailabilityUpdateDateRange):
            available_rooms (int): Rooms to sell (`roomstosell`). `0` blocks the room for the range.
            status (BookingAvailabilityUpdateStatus | Unset):
            closed (bool | None | Unset): Dedicated stop-sell flag (`<closed>` in Booking's XML). `true` fully stops sale
                for the room/date-range regardless of `availableRooms`.
            restrictions (BookingPricingRateUpdateRestrictions | Unset): Optional length-of-stay / availability restrictions
                for one rate update. Every field here is forwarded verbatim into Booking.com's rates XML (`minimumstay`,
                `maximumstay`, `closedonarrival`, `closedondeparture`, …) — omit a field to leave that restriction untouched.
     """

    room_id: str
    rate_id: str
    date_range: BookingAvailabilityUpdateDateRange
    available_rooms: int
    status: BookingAvailabilityUpdateStatus | Unset = UNSET
    closed: bool | None | Unset = UNSET
    restrictions: BookingPricingRateUpdateRestrictions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_availability_update_date_range import BookingAvailabilityUpdateDateRange
        from ..models.booking_pricing_rate_update_restrictions import BookingPricingRateUpdateRestrictions
        room_id = self.room_id

        rate_id = self.rate_id

        date_range = self.date_range.to_dict()

        available_rooms = self.available_rooms

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        closed: bool | None | Unset
        if isinstance(self.closed, Unset):
            closed = UNSET
        else:
            closed = self.closed

        restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomId": room_id,
            "rateId": rate_id,
            "dateRange": date_range,
            "availableRooms": available_rooms,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if closed is not UNSET:
            field_dict["closed"] = closed
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_availability_update_date_range import BookingAvailabilityUpdateDateRange
        from ..models.booking_pricing_rate_update_restrictions import BookingPricingRateUpdateRestrictions
        d = dict(src_dict)
        room_id = d.pop("roomId")

        rate_id = d.pop("rateId")

        date_range = BookingAvailabilityUpdateDateRange.from_dict(d.pop("dateRange"))




        available_rooms = d.pop("availableRooms")

        _status = d.pop("status", UNSET)
        status: BookingAvailabilityUpdateStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BookingAvailabilityUpdateStatus(_status)




        def _parse_closed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed = _parse_closed(d.pop("closed", UNSET))


        _restrictions = d.pop("restrictions", UNSET)
        restrictions: BookingPricingRateUpdateRestrictions | Unset
        if isinstance(_restrictions,  Unset):
            restrictions = UNSET
        else:
            restrictions = BookingPricingRateUpdateRestrictions.from_dict(_restrictions)




        booking_availability_update = cls(
            room_id=room_id,
            rate_id=rate_id,
            date_range=date_range,
            available_rooms=available_rooms,
            status=status,
            closed=closed,
            restrictions=restrictions,
        )


        booking_availability_update.additional_properties = d
        return booking_availability_update

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
