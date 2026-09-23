from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_property_action_request_action import BookingPropertyActionRequestAction
from ..types import UNSET, Unset






T = TypeVar("T", bound="BookingPropertyActionRequest")



@_attrs_define
class BookingPropertyActionRequest:
    """ Take this listing's Booking.com property off sale, or put it back.

        Attributes:
            action (BookingPropertyActionRequestAction): `unlist` closes the room's availability across the whole forward
                window, so the property stops selling. `relist` re-syncs the real calendar: dates that are genuinely blocked (a
                reservation, an owner stay) stay blocked, and only the closure `unlist` wrote lifts. They are not mirror images,
                and that is deliberate.
            hotel_id (str | Unset): Booking.com property to act on, for a listing mapped to more than one. Without it the
                request is refused with `409 ambiguous_booking_mapping` and nothing is written. `?hotel_id=` means the same
                thing; the body wins if you send both.
     """

    action: BookingPropertyActionRequestAction
    hotel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        hotel_id = self.hotel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = BookingPropertyActionRequestAction(d.pop("action"))




        hotel_id = d.pop("hotelId", UNSET)

        booking_property_action_request = cls(
            action=action,
            hotel_id=hotel_id,
        )


        booking_property_action_request.additional_properties = d
        return booking_property_action_request

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
