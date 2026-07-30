from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SandboxResetResultDeleted")



@_attrs_define
class SandboxResetResultDeleted:
    """ 
        Attributes:
            listings (int):  Example: 3.
            reservations (int):  Example: 5.
            connections (int):  Example: 2.
     """

    listings: int
    reservations: int
    connections: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listings = self.listings

        reservations = self.reservations

        connections = self.connections


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listings": listings,
            "reservations": reservations,
            "connections": connections,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listings = d.pop("listings")

        reservations = d.pop("reservations")

        connections = d.pop("connections")

        sandbox_reset_result_deleted = cls(
            listings=listings,
            reservations=reservations,
            connections=connections,
        )


        sandbox_reset_result_deleted.additional_properties = d
        return sandbox_reset_result_deleted

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
