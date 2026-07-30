from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbAlteration")



@_attrs_define
class AirbnbAlteration:
    """ An Airbnb reservation alteration request (date change, guest-count change, or price change), mirrored locally in
    `reservation_alterations`. Additional Airbnb-side fields may be present.

        Attributes:
            alteration_id (None | str | Unset): Airbnb alteration id.
            reservation_id (int | None | Unset): Repull reservation id the alteration belongs to.
            platform (str | Unset):  Example: airbnb.
            status (None | str | Unset): Alteration status (e.g. `pending`).
            created_at (datetime.datetime | None | Unset):
     """

    alteration_id: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    platform: str | Unset = UNSET
    status: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        alteration_id: None | str | Unset
        if isinstance(self.alteration_id, Unset):
            alteration_id = UNSET
        else:
            alteration_id = self.alteration_id

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        platform = self.platform

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alteration_id is not UNSET:
            field_dict["alterationId"] = alteration_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_alteration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alteration_id = _parse_alteration_id(d.pop("alterationId", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        platform = d.pop("platform", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        airbnb_alteration = cls(
            alteration_id=alteration_id,
            reservation_id=reservation_id,
            platform=platform,
            status=status,
            created_at=created_at,
        )


        airbnb_alteration.additional_properties = d
        return airbnb_alteration

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
