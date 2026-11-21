from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_fees_body_extra_guests_type_0_type import UpdateVrboListingFeesBodyExtraGuestsType0Type
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingFeesBodyExtraGuestsType0")



@_attrs_define
class UpdateVrboListingFeesBodyExtraGuestsType0:
    """ 
        Attributes:
            amount (float | Unset):
            type_ (UpdateVrboListingFeesBodyExtraGuestsType0Type | Unset):
            after_guests (int | Unset):
            taxable (bool | Unset):
     """

    amount: float | Unset = UNSET
    type_: UpdateVrboListingFeesBodyExtraGuestsType0Type | Unset = UNSET
    after_guests: int | Unset = UNSET
    taxable: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        after_guests = self.after_guests

        taxable = self.taxable


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if type_ is not UNSET:
            field_dict["type"] = type_
        if after_guests is not UNSET:
            field_dict["afterGuests"] = after_guests
        if taxable is not UNSET:
            field_dict["taxable"] = taxable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UpdateVrboListingFeesBodyExtraGuestsType0Type | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = UpdateVrboListingFeesBodyExtraGuestsType0Type(_type_)




        after_guests = d.pop("afterGuests", UNSET)

        taxable = d.pop("taxable", UNSET)

        update_vrbo_listing_fees_body_extra_guests_type_0 = cls(
            amount=amount,
            type_=type_,
            after_guests=after_guests,
            taxable=taxable,
        )

        return update_vrbo_listing_fees_body_extra_guests_type_0

