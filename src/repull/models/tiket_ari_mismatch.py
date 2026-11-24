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






T = TypeVar("T", bound="TiketAriMismatch")



@_attrs_define
class TiketAriMismatch:
    """ A night where what tiket.com holds after the write differs from what was sent.

        Attributes:
            date (datetime.date | Unset):
            room_type_code (str | Unset):
            rate_plan_code (None | str | Unset):
            field (str | Unset):  Example: price.
            sent (Any | Unset): The value sent.
            read (Any | Unset): The value tiket.com returned.
     """

    date: datetime.date | Unset = UNSET
    room_type_code: str | Unset = UNSET
    rate_plan_code: None | str | Unset = UNSET
    field: str | Unset = UNSET
    sent: Any | Unset = UNSET
    read: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        room_type_code = self.room_type_code

        rate_plan_code: None | str | Unset
        if isinstance(self.rate_plan_code, Unset):
            rate_plan_code = UNSET
        else:
            rate_plan_code = self.rate_plan_code

        field = self.field

        sent = self.sent

        read = self.read


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if room_type_code is not UNSET:
            field_dict["roomTypeCode"] = room_type_code
        if rate_plan_code is not UNSET:
            field_dict["ratePlanCode"] = rate_plan_code
        if field is not UNSET:
            field_dict["field"] = field
        if sent is not UNSET:
            field_dict["sent"] = sent
        if read is not UNSET:
            field_dict["read"] = read

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        room_type_code = d.pop("roomTypeCode", UNSET)

        def _parse_rate_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_plan_code = _parse_rate_plan_code(d.pop("ratePlanCode", UNSET))


        field = d.pop("field", UNSET)

        sent = d.pop("sent", UNSET)

        read = d.pop("read", UNSET)

        tiket_ari_mismatch = cls(
            date=date,
            room_type_code=room_type_code,
            rate_plan_code=rate_plan_code,
            field=field,
            sent=sent,
            read=read,
        )


        tiket_ari_mismatch.additional_properties = d
        return tiket_ari_mismatch

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
