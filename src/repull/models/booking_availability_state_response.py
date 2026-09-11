from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BookingAvailabilityStateResponse")



@_attrs_define
class BookingAvailabilityStateResponse:
    """ Returned by `GET /v1/channels/booking/availability`. Proxies Booking's `getRoomRateAvailability` — current rate /
    availability / restriction state per room + rate plan for the requested window, keyed by `property_id`. Field set is
    whatever Booking.com emits (parsed from their XML), so the object is open-ended.

        Attributes:
            property_id (str | Unset): Booking.com hotel/property id echoed back.
     """

    property_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["property_id"] = property_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_id = d.pop("property_id", UNSET)

        booking_availability_state_response = cls(
            property_id=property_id,
        )


        booking_availability_state_response.additional_properties = d
        return booking_availability_state_response

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
