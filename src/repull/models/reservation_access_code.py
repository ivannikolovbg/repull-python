from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_access_code_type import ReservationAccessCodeType
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_access_code_locks_item import ReservationAccessCodeLocksItem





T = TypeVar("T", bound="ReservationAccessCode")



@_attrs_define
class ReservationAccessCode:
    """ One door code for a stay, as the PMS reported it.

        Attributes:
            code (str): The code to enter on the lock. Example: 482913.
            type_ (ReservationAccessCodeType): `guest`: the code to give the guest. `backup`: give it only if the guest code
                fails; Guesty may change a backup code read before check-in day. Example: guest.
            status (None | str): The PMS's status for the code, lower-cased. Example: active.
            valid_from (datetime.datetime | None): When the code starts working. `null` when the PMS gives no window.
                Example: 2026-11-01T20:00:00.000Z.
            valid_until (datetime.datetime | None): When the code stops working. `null` when the PMS gives no window.
                Example: 2026-11-05T15:00:00.000Z.
            locks (list[ReservationAccessCodeLocksItem]): The locks the code opens.
            source (str): The PMS the code was read from. Example: guesty.
            updated_at (datetime.datetime | None): When the codes were last read from the PMS. Example:
                2026-10-31T14:30:00.000Z.
     """

    code: str
    type_: ReservationAccessCodeType
    status: None | str
    valid_from: datetime.datetime | None
    valid_until: datetime.datetime | None
    locks: list[ReservationAccessCodeLocksItem]
    source: str
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_access_code_locks_item import ReservationAccessCodeLocksItem
        code = self.code

        type_ = self.type_.value

        status: None | str
        status = self.status

        valid_from: None | str
        if isinstance(self.valid_from, datetime.datetime):
            valid_from = self.valid_from.isoformat()
        else:
            valid_from = self.valid_from

        valid_until: None | str
        if isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        locks = []
        for locks_item_data in self.locks:
            locks_item = locks_item_data.to_dict()
            locks.append(locks_item)



        source = self.source

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "type": type_,
            "status": status,
            "validFrom": valid_from,
            "validUntil": valid_until,
            "locks": locks,
            "source": source,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_access_code_locks_item import ReservationAccessCodeLocksItem
        d = dict(src_dict)
        code = d.pop("code")

        type_ = ReservationAccessCodeType(d.pop("type"))




        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))


        def _parse_valid_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_type_0 = isoparse(data)



                return valid_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        valid_from = _parse_valid_from(d.pop("validFrom"))


        def _parse_valid_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = isoparse(data)



                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        valid_until = _parse_valid_until(d.pop("validUntil"))


        locks = []
        _locks = d.pop("locks")
        for locks_item_data in (_locks):
            locks_item = ReservationAccessCodeLocksItem.from_dict(locks_item_data)



            locks.append(locks_item)


        source = d.pop("source")

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))


        reservation_access_code = cls(
            code=code,
            type_=type_,
            status=status,
            valid_from=valid_from,
            valid_until=valid_until,
            locks=locks,
            source=source,
            updated_at=updated_at,
        )


        reservation_access_code.additional_properties = d
        return reservation_access_code

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
