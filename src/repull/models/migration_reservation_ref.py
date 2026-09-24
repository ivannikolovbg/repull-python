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






T = TypeVar("T", bound="MigrationReservationRef")



@_attrs_define
class MigrationReservationRef:
    """ 
        Attributes:
            confirmation_code (str | Unset):
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            reservation_id (str | Unset):
            platform (None | str | Unset):
     """

    confirmation_code: str | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    reservation_id: str | Unset = UNSET
    platform: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        reservation_id = self.reservation_id

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmationCode", UNSET)

        _check_in = d.pop("checkIn", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("checkOut", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        reservation_id = d.pop("reservationId", UNSET)

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))


        migration_reservation_ref = cls(
            confirmation_code=confirmation_code,
            check_in=check_in,
            check_out=check_out,
            reservation_id=reservation_id,
            platform=platform,
        )


        migration_reservation_ref.additional_properties = d
        return migration_reservation_ref

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
