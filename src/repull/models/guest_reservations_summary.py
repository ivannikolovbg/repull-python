from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GuestReservationsSummary")



@_attrs_define
class GuestReservationsSummary:
    """ Aggregate counts of reservations attached to the guest. `future` is derived from `total - past - cancelled`.

        Attributes:
            total (int | Unset):
            future (int | Unset):
            past (int | Unset):
            cancelled (int | Unset):
     """

    total: int | Unset = UNSET
    future: int | Unset = UNSET
    past: int | Unset = UNSET
    cancelled: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        future = self.future

        past = self.past

        cancelled = self.cancelled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if future is not UNSET:
            field_dict["future"] = future
        if past is not UNSET:
            field_dict["past"] = past
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        future = d.pop("future", UNSET)

        past = d.pop("past", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        guest_reservations_summary = cls(
            total=total,
            future=future,
            past=past,
            cancelled=cancelled,
        )


        guest_reservations_summary.additional_properties = d
        return guest_reservations_summary

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
