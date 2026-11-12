from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.map_connect_booking_rooms_response_property_status_type_0_outcome import MapConnectBookingRoomsResponsePropertyStatusType0Outcome
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MapConnectBookingRoomsResponsePropertyStatusType0")



@_attrs_define
class MapConnectBookingRoomsResponsePropertyStatusType0:
    """ Whether Booking.com has the property open for bookings. A property still being built on Booking.com is checked and
    opened as the last Connect step; one that is already open, or that its host closed, is left as it is. `null` when no
    room was mapped.

        Attributes:
            property_id (str | Unset):
            outcome (MapConnectBookingRoomsResponsePropertyStatusType0Outcome | Unset): `opened`: it was being built and is
                now open. `not_needed`: it was already past that stage. `blocked`: Booking.com will not open it yet — see
                `blockers`. `status_unknown`: its status could not be read. `failed`: Booking.com did not answer the open
                request.
            status_before (None | str | Unset): Booking.com's status for the property before this step, e.g. `XML: Being
                built`.
            blockers (list[str] | Unset): Booking.com's own reasons it will not open the property yet.
            message (None | str | Unset): What is wrong and how to fix it, in plain words. Null when the property is open.
     """

    property_id: str | Unset = UNSET
    outcome: MapConnectBookingRoomsResponsePropertyStatusType0Outcome | Unset = UNSET
    status_before: None | str | Unset = UNSET
    blockers: list[str] | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value


        status_before: None | str | Unset
        if isinstance(self.status_before, Unset):
            status_before = UNSET
        else:
            status_before = self.status_before

        blockers: list[str] | Unset = UNSET
        if not isinstance(self.blockers, Unset):
            blockers = self.blockers



        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if status_before is not UNSET:
            field_dict["statusBefore"] = status_before
        if blockers is not UNSET:
            field_dict["blockers"] = blockers
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_id = d.pop("propertyId", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: MapConnectBookingRoomsResponsePropertyStatusType0Outcome | Unset
        if isinstance(_outcome,  Unset):
            outcome = UNSET
        else:
            outcome = MapConnectBookingRoomsResponsePropertyStatusType0Outcome(_outcome)




        def _parse_status_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_before = _parse_status_before(d.pop("statusBefore", UNSET))


        blockers = cast(list[str], d.pop("blockers", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        map_connect_booking_rooms_response_property_status_type_0 = cls(
            property_id=property_id,
            outcome=outcome,
            status_before=status_before,
            blockers=blockers,
            message=message,
        )


        map_connect_booking_rooms_response_property_status_type_0.additional_properties = d
        return map_connect_booking_rooms_response_property_status_type_0

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
