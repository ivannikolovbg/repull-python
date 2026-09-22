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






T = TypeVar("T", bound="BookingRestrictionRequestRow")



@_attrs_define
class BookingRestrictionRequestRow:
    """ One update's restriction request: which nights, and which restrictions were asked for them.

        Attributes:
            index (int | Unset): Position of the update in the request `updates[]`.
            room_id (str | Unset):
            rate_id (str | Unset):
            start (datetime.date | Unset): First night, inclusive.
            end (datetime.date | Unset): Last night, inclusive.
            fields (list[str] | Unset): The restrictions stated for these nights.
     """

    index: int | Unset = UNSET
    room_id: str | Unset = UNSET
    rate_id: str | Unset = UNSET
    start: datetime.date | Unset = UNSET
    end: datetime.date | Unset = UNSET
    fields: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        index = self.index

        room_id = self.room_id

        rate_id = self.rate_id

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if rate_id is not UNSET:
            field_dict["rateId"] = rate_id
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        room_id = d.pop("roomId", UNSET)

        rate_id = d.pop("rateId", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.date | Unset
        if isinstance(_start,  Unset):
            start = UNSET
        else:
            start = isoparse(_start).date()




        _end = d.pop("end", UNSET)
        end: datetime.date | Unset
        if isinstance(_end,  Unset):
            end = UNSET
        else:
            end = isoparse(_end).date()




        fields = cast(list[str], d.pop("fields", UNSET))


        booking_restriction_request_row = cls(
            index=index,
            room_id=room_id,
            rate_id=rate_id,
            start=start,
            end=end,
            fields=fields,
        )


        booking_restriction_request_row.additional_properties = d
        return booking_restriction_request_row

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
