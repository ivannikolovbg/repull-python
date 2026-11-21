from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingFeesResponse200DataCleaningType0")



@_attrs_define
class GetVrboListingFeesResponse200DataCleaningType0:
    """ 
        Attributes:
            amount (float | None | Unset):
            type_ (None | str | Unset):  Example: PER_STAY.
            taxable (bool | None | Unset):
     """

    amount: float | None | Unset = UNSET
    type_: None | str | Unset = UNSET
    taxable: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        taxable: bool | None | Unset
        if isinstance(self.taxable, Unset):
            taxable = UNSET
        else:
            taxable = self.taxable


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if type_ is not UNSET:
            field_dict["type"] = type_
        if taxable is not UNSET:
            field_dict["taxable"] = taxable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_taxable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        taxable = _parse_taxable(d.pop("taxable", UNSET))


        get_vrbo_listing_fees_response_200_data_cleaning_type_0 = cls(
            amount=amount,
            type_=type_,
            taxable=taxable,
        )


        get_vrbo_listing_fees_response_200_data_cleaning_type_0.additional_properties = d
        return get_vrbo_listing_fees_response_200_data_cleaning_type_0

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
