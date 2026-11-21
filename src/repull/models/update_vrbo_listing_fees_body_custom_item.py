from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_fees_body_custom_item_type import UpdateVrboListingFeesBodyCustomItemType
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingFeesBodyCustomItem")



@_attrs_define
class UpdateVrboListingFeesBodyCustomItem:
    """ 
        Attributes:
            product_code (str): One of the read's `customFeeCodes` (e.g. ADMINISTRATIVE, HOT_TUB, LINENS, PARKING, POOL).
                Example: PARKING.
            amount (float):
            type_ (UpdateVrboListingFeesBodyCustomItemType | Unset):
            taxable (bool | Unset):
            tax_rate (float | Unset):
     """

    product_code: str
    amount: float
    type_: UpdateVrboListingFeesBodyCustomItemType | Unset = UNSET
    taxable: bool | Unset = UNSET
    tax_rate: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        product_code = self.product_code

        amount = self.amount

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        taxable = self.taxable

        tax_rate = self.tax_rate


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "productCode": product_code,
            "amount": amount,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if taxable is not UNSET:
            field_dict["taxable"] = taxable
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_code = d.pop("productCode")

        amount = d.pop("amount")

        _type_ = d.pop("type", UNSET)
        type_: UpdateVrboListingFeesBodyCustomItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = UpdateVrboListingFeesBodyCustomItemType(_type_)




        taxable = d.pop("taxable", UNSET)

        tax_rate = d.pop("taxRate", UNSET)

        update_vrbo_listing_fees_body_custom_item = cls(
            product_code=product_code,
            amount=amount,
            type_=type_,
            taxable=taxable,
            tax_rate=tax_rate,
        )

        return update_vrbo_listing_fees_body_custom_item

