from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingTaxesBodyStayTax")



@_attrs_define
class UpdateVrboListingTaxesBodyStayTax:
    """ 
        Attributes:
            amount (float):
            min_age (int | Unset):
     """

    amount: float
    min_age: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        min_age = self.min_age


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "amount": amount,
        })
        if min_age is not UNSET:
            field_dict["minAge"] = min_age

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        min_age = d.pop("minAge", UNSET)

        update_vrbo_listing_taxes_body_stay_tax = cls(
            amount=amount,
            min_age=min_age,
        )

        return update_vrbo_listing_taxes_body_stay_tax

