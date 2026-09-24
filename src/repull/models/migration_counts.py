from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MigrationCounts")



@_attrs_define
class MigrationCounts:
    """ 
        Attributes:
            listings (int | Unset):
            reservations (int | Unset):
            upcoming_reservations (int | Unset):
            guests (int | Unset):
            conversations (int | Unset):
     """

    listings: int | Unset = UNSET
    reservations: int | Unset = UNSET
    upcoming_reservations: int | Unset = UNSET
    guests: int | Unset = UNSET
    conversations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listings = self.listings

        reservations = self.reservations

        upcoming_reservations = self.upcoming_reservations

        guests = self.guests

        conversations = self.conversations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listings is not UNSET:
            field_dict["listings"] = listings
        if reservations is not UNSET:
            field_dict["reservations"] = reservations
        if upcoming_reservations is not UNSET:
            field_dict["upcomingReservations"] = upcoming_reservations
        if guests is not UNSET:
            field_dict["guests"] = guests
        if conversations is not UNSET:
            field_dict["conversations"] = conversations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listings = d.pop("listings", UNSET)

        reservations = d.pop("reservations", UNSET)

        upcoming_reservations = d.pop("upcomingReservations", UNSET)

        guests = d.pop("guests", UNSET)

        conversations = d.pop("conversations", UNSET)

        migration_counts = cls(
            listings=listings,
            reservations=reservations,
            upcoming_reservations=upcoming_reservations,
            guests=guests,
            conversations=conversations,
        )


        migration_counts.additional_properties = d
        return migration_counts

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
