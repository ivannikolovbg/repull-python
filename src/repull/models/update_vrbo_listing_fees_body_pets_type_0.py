from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_fees_body_pets_type_0_type import UpdateVrboListingFeesBodyPetsType0Type
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingFeesBodyPetsType0")



@_attrs_define
class UpdateVrboListingFeesBodyPetsType0:
    """ 
        Attributes:
            amount (float):
            type_ (UpdateVrboListingFeesBodyPetsType0Type | Unset):
            taxable (bool | Unset):
     """

    amount: float
    type_: UpdateVrboListingFeesBodyPetsType0Type | Unset = UNSET
    taxable: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        taxable = self.taxable


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "amount": amount,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if taxable is not UNSET:
            field_dict["taxable"] = taxable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        _type_ = d.pop("type", UNSET)
        type_: UpdateVrboListingFeesBodyPetsType0Type | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = UpdateVrboListingFeesBodyPetsType0Type(_type_)




        taxable = d.pop("taxable", UNSET)

        update_vrbo_listing_fees_body_pets_type_0 = cls(
            amount=amount,
            type_=type_,
            taxable=taxable,
        )

        return update_vrbo_listing_fees_body_pets_type_0

