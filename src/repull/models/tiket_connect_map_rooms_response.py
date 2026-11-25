from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TiketConnectMapRoomsResponse")



@_attrs_define
class TiketConnectMapRoomsResponse:
    """ 
        Attributes:
            success (bool | Unset):
            session_id (str | Unset):
            connection_id (None | str | Unset):
            mapped (int | Unset):
            unmapped (int | Unset):
            created (int | Unset): Listings created from rooms (`create: true`).
            replayed_reservations (int | Unset): Bookings tiket.com delivered before the rooms were mapped, now recorded.
     """

    success: bool | Unset = UNSET
    session_id: str | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    mapped: int | Unset = UNSET
    unmapped: int | Unset = UNSET
    created: int | Unset = UNSET
    replayed_reservations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        session_id = self.session_id

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        mapped = self.mapped

        unmapped = self.unmapped

        created = self.created

        replayed_reservations = self.replayed_reservations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success is not UNSET:
            field_dict["success"] = success
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if mapped is not UNSET:
            field_dict["mapped"] = mapped
        if unmapped is not UNSET:
            field_dict["unmapped"] = unmapped
        if created is not UNSET:
            field_dict["created"] = created
        if replayed_reservations is not UNSET:
            field_dict["replayedReservations"] = replayed_reservations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        session_id = d.pop("sessionId", UNSET)

        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        mapped = d.pop("mapped", UNSET)

        unmapped = d.pop("unmapped", UNSET)

        created = d.pop("created", UNSET)

        replayed_reservations = d.pop("replayedReservations", UNSET)

        tiket_connect_map_rooms_response = cls(
            success=success,
            session_id=session_id,
            connection_id=connection_id,
            mapped=mapped,
            unmapped=unmapped,
            created=created,
            replayed_reservations=replayed_reservations,
        )


        tiket_connect_map_rooms_response.additional_properties = d
        return tiket_connect_map_rooms_response

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
