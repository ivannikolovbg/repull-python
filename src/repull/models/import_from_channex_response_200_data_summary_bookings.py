from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportFromChannexResponse200DataSummaryBookings")



@_attrs_define
class ImportFromChannexResponse200DataSummaryBookings:
    """ 
        Attributes:
            read (int | Unset):
            linked (int | Unset):
            waiting (int | Unset):
     """

    read: int | Unset = UNSET
    linked: int | Unset = UNSET
    waiting: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        read = self.read

        linked = self.linked

        waiting = self.waiting


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if read is not UNSET:
            field_dict["read"] = read
        if linked is not UNSET:
            field_dict["linked"] = linked
        if waiting is not UNSET:
            field_dict["waiting"] = waiting

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = d.pop("read", UNSET)

        linked = d.pop("linked", UNSET)

        waiting = d.pop("waiting", UNSET)

        import_from_channex_response_200_data_summary_bookings = cls(
            read=read,
            linked=linked,
            waiting=waiting,
        )


        import_from_channex_response_200_data_summary_bookings.additional_properties = d
        return import_from_channex_response_200_data_summary_bookings

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
