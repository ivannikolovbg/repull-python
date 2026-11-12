from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.map_connect_booking_rooms_response_property_status_type_0 import MapConnectBookingRoomsResponsePropertyStatusType0





T = TypeVar("T", bound="MapConnectBookingRoomsResponse")



@_attrs_define
class MapConnectBookingRoomsResponse:
    """ 
        Attributes:
            success (bool):  Example: True.
            mapped (int): Rooms now linked to a listing.
            session_id (str):
            connection_id (str):
            needs_calendar (list[str]): Ids of the listings this call created from Booking.com rooms (`create: true`). They
                start without a calendar: Booking.com shows those rooms closed and nothing is sent to Booking.com for them until
                they have one. Give a listing a calendar by setting its prices and availability with `PUT
                /v1/availability/{propertyId}`, or by mapping the same home from Airbnb so its calendar is used. Rooms mapped to
                an existing listing are not listed: that listing's calendar is pushed as before.
            unmapped (int | Unset): Rooms submitted with `listingId: null` ("don't map"), which are left without a listing.
            reservations_imported (int | None | Unset): Reservations pulled from Booking.com once the rooms were mapped.
                Mapping triggers the same full property sync the dashboard's Sync button runs, because a reservation can only be
                resolved to a listing through a mapped room. `0` without a sync when no room was mapped. `null` means the sync
                could not be run — the connection and mapping are still good, and the property can be synced from the dashboard.
            reservations_found (int | None | Unset): How many reservations Booking.com returned for the property. Equal to
                `reservationsImported` unless some could not be attached to a listing — so `0` here means Booking.com had none.
                `null` when the sync could not run.
            calendar_note (str | Unset): Plain-language explanation of `needsCalendar`, present only when it is non-empty.
            property_status (MapConnectBookingRoomsResponsePropertyStatusType0 | None | Unset): Whether Booking.com has the
                property open for bookings. A property still being built on Booking.com is checked and opened as the last
                Connect step; one that is already open, or that its host closed, is left as it is. `null` when no room was
                mapped.
            property_note (str | Unset): `propertyStatus.message`, present only when the property is not open.
     """

    success: bool
    mapped: int
    session_id: str
    connection_id: str
    needs_calendar: list[str]
    unmapped: int | Unset = UNSET
    reservations_imported: int | None | Unset = UNSET
    reservations_found: int | None | Unset = UNSET
    calendar_note: str | Unset = UNSET
    property_status: MapConnectBookingRoomsResponsePropertyStatusType0 | None | Unset = UNSET
    property_note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.map_connect_booking_rooms_response_property_status_type_0 import MapConnectBookingRoomsResponsePropertyStatusType0
        success = self.success

        mapped = self.mapped

        session_id = self.session_id

        connection_id = self.connection_id

        needs_calendar = self.needs_calendar



        unmapped = self.unmapped

        reservations_imported: int | None | Unset
        if isinstance(self.reservations_imported, Unset):
            reservations_imported = UNSET
        else:
            reservations_imported = self.reservations_imported

        reservations_found: int | None | Unset
        if isinstance(self.reservations_found, Unset):
            reservations_found = UNSET
        else:
            reservations_found = self.reservations_found

        calendar_note = self.calendar_note

        property_status: dict[str, Any] | None | Unset
        if isinstance(self.property_status, Unset):
            property_status = UNSET
        elif isinstance(self.property_status, MapConnectBookingRoomsResponsePropertyStatusType0):
            property_status = self.property_status.to_dict()
        else:
            property_status = self.property_status

        property_note = self.property_note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "mapped": mapped,
            "sessionId": session_id,
            "connectionId": connection_id,
            "needsCalendar": needs_calendar,
        })
        if unmapped is not UNSET:
            field_dict["unmapped"] = unmapped
        if reservations_imported is not UNSET:
            field_dict["reservationsImported"] = reservations_imported
        if reservations_found is not UNSET:
            field_dict["reservationsFound"] = reservations_found
        if calendar_note is not UNSET:
            field_dict["calendarNote"] = calendar_note
        if property_status is not UNSET:
            field_dict["propertyStatus"] = property_status
        if property_note is not UNSET:
            field_dict["propertyNote"] = property_note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_connect_booking_rooms_response_property_status_type_0 import MapConnectBookingRoomsResponsePropertyStatusType0
        d = dict(src_dict)
        success = d.pop("success")

        mapped = d.pop("mapped")

        session_id = d.pop("sessionId")

        connection_id = d.pop("connectionId")

        needs_calendar = cast(list[str], d.pop("needsCalendar"))


        unmapped = d.pop("unmapped", UNSET)

        def _parse_reservations_imported(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservations_imported = _parse_reservations_imported(d.pop("reservationsImported", UNSET))


        def _parse_reservations_found(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservations_found = _parse_reservations_found(d.pop("reservationsFound", UNSET))


        calendar_note = d.pop("calendarNote", UNSET)

        def _parse_property_status(data: object) -> MapConnectBookingRoomsResponsePropertyStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                property_status_type_0 = MapConnectBookingRoomsResponsePropertyStatusType0.from_dict(data)



                return property_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MapConnectBookingRoomsResponsePropertyStatusType0 | None | Unset, data)

        property_status = _parse_property_status(d.pop("propertyStatus", UNSET))


        property_note = d.pop("propertyNote", UNSET)

        map_connect_booking_rooms_response = cls(
            success=success,
            mapped=mapped,
            session_id=session_id,
            connection_id=connection_id,
            needs_calendar=needs_calendar,
            unmapped=unmapped,
            reservations_imported=reservations_imported,
            reservations_found=reservations_found,
            calendar_note=calendar_note,
            property_status=property_status,
            property_note=property_note,
        )


        map_connect_booking_rooms_response.additional_properties = d
        return map_connect_booking_rooms_response

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
