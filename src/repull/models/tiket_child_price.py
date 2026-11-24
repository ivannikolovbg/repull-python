from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TiketChildPrice")



@_attrs_define
class TiketChildPrice:
    """ Price for a child in an age band. The age bands must match the ones set in the tiket.com extranet.

        Attributes:
            min_age (int):
            max_age (int):  Example: 11.
            amount (float):  Example: 100000.
     """

    min_age: int
    max_age: int
    amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_age = self.min_age

        max_age = self.max_age

        amount = self.amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "minAge": min_age,
            "maxAge": max_age,
            "amount": amount,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_age = d.pop("minAge")

        max_age = d.pop("maxAge")

        amount = d.pop("amount")

        tiket_child_price = cls(
            min_age=min_age,
            max_age=max_age,
            amount=amount,
        )


        tiket_child_price.additional_properties = d
        return tiket_child_price

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
