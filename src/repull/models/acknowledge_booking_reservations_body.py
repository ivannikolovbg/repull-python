from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AcknowledgeBookingReservationsBody")



@_attrs_define
class AcknowledgeBookingReservationsBody:
    """ 
        Attributes:
            reservation_ids (list[str]): Booking.com reservation ids to acknowledge.
     """

    reservation_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_ids = self.reservation_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservation_ids": reservation_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservation_ids = cast(list[str], d.pop("reservation_ids"))


        acknowledge_booking_reservations_body = cls(
            reservation_ids=reservation_ids,
        )


        acknowledge_booking_reservations_body.additional_properties = d
        return acknowledge_booking_reservations_body

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
