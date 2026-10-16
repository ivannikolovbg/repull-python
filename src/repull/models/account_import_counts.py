from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AccountImportCounts")



@_attrs_define
class AccountImportCounts:
    """ What the import brought in. A channel reports the keys it imports.

        Attributes:
            listings (int | Unset):
            reservations (int | Unset):
            conversations (int | Unset):
            messages (int | Unset):
            reviews (int | Unset):
            payments (int | Unset):
     """

    listings: int | Unset = UNSET
    reservations: int | Unset = UNSET
    conversations: int | Unset = UNSET
    messages: int | Unset = UNSET
    reviews: int | Unset = UNSET
    payments: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listings = self.listings

        reservations = self.reservations

        conversations = self.conversations

        messages = self.messages

        reviews = self.reviews

        payments = self.payments


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listings is not UNSET:
            field_dict["listings"] = listings
        if reservations is not UNSET:
            field_dict["reservations"] = reservations
        if conversations is not UNSET:
            field_dict["conversations"] = conversations
        if messages is not UNSET:
            field_dict["messages"] = messages
        if reviews is not UNSET:
            field_dict["reviews"] = reviews
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listings = d.pop("listings", UNSET)

        reservations = d.pop("reservations", UNSET)

        conversations = d.pop("conversations", UNSET)

        messages = d.pop("messages", UNSET)

        reviews = d.pop("reviews", UNSET)

        payments = d.pop("payments", UNSET)

        account_import_counts = cls(
            listings=listings,
            reservations=reservations,
            conversations=conversations,
            messages=messages,
            reviews=reviews,
            payments=payments,
        )


        account_import_counts.additional_properties = d
        return account_import_counts

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
