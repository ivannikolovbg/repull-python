from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="QuotePricing")



@_attrs_define
class QuotePricing:
    """ 
        Attributes:
            nightly_total (float | None | Unset):
            length_of_stay_discount (float | None | Unset):
            length_of_stay_discount_percent (float | None | Unset):
            cleaning_fee (float | None | Unset):
            pet_fee (float | None | Unset):
            other_fees (float | None | Unset):
            taxes (float | None | Unset):
            total (float | None | Unset):
     """

    nightly_total: float | None | Unset = UNSET
    length_of_stay_discount: float | None | Unset = UNSET
    length_of_stay_discount_percent: float | None | Unset = UNSET
    cleaning_fee: float | None | Unset = UNSET
    pet_fee: float | None | Unset = UNSET
    other_fees: float | None | Unset = UNSET
    taxes: float | None | Unset = UNSET
    total: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        nightly_total: float | None | Unset
        if isinstance(self.nightly_total, Unset):
            nightly_total = UNSET
        else:
            nightly_total = self.nightly_total

        length_of_stay_discount: float | None | Unset
        if isinstance(self.length_of_stay_discount, Unset):
            length_of_stay_discount = UNSET
        else:
            length_of_stay_discount = self.length_of_stay_discount

        length_of_stay_discount_percent: float | None | Unset
        if isinstance(self.length_of_stay_discount_percent, Unset):
            length_of_stay_discount_percent = UNSET
        else:
            length_of_stay_discount_percent = self.length_of_stay_discount_percent

        cleaning_fee: float | None | Unset
        if isinstance(self.cleaning_fee, Unset):
            cleaning_fee = UNSET
        else:
            cleaning_fee = self.cleaning_fee

        pet_fee: float | None | Unset
        if isinstance(self.pet_fee, Unset):
            pet_fee = UNSET
        else:
            pet_fee = self.pet_fee

        other_fees: float | None | Unset
        if isinstance(self.other_fees, Unset):
            other_fees = UNSET
        else:
            other_fees = self.other_fees

        taxes: float | None | Unset
        if isinstance(self.taxes, Unset):
            taxes = UNSET
        else:
            taxes = self.taxes

        total: float | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if nightly_total is not UNSET:
            field_dict["nightlyTotal"] = nightly_total
        if length_of_stay_discount is not UNSET:
            field_dict["lengthOfStayDiscount"] = length_of_stay_discount
        if length_of_stay_discount_percent is not UNSET:
            field_dict["lengthOfStayDiscountPercent"] = length_of_stay_discount_percent
        if cleaning_fee is not UNSET:
            field_dict["cleaningFee"] = cleaning_fee
        if pet_fee is not UNSET:
            field_dict["petFee"] = pet_fee
        if other_fees is not UNSET:
            field_dict["otherFees"] = other_fees
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_nightly_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nightly_total = _parse_nightly_total(d.pop("nightlyTotal", UNSET))


        def _parse_length_of_stay_discount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        length_of_stay_discount = _parse_length_of_stay_discount(d.pop("lengthOfStayDiscount", UNSET))


        def _parse_length_of_stay_discount_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        length_of_stay_discount_percent = _parse_length_of_stay_discount_percent(d.pop("lengthOfStayDiscountPercent", UNSET))


        def _parse_cleaning_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cleaning_fee = _parse_cleaning_fee(d.pop("cleaningFee", UNSET))


        def _parse_pet_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pet_fee = _parse_pet_fee(d.pop("petFee", UNSET))


        def _parse_other_fees(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        other_fees = _parse_other_fees(d.pop("otherFees", UNSET))


        def _parse_taxes(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        taxes = _parse_taxes(d.pop("taxes", UNSET))


        def _parse_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))


        quote_pricing = cls(
            nightly_total=nightly_total,
            length_of_stay_discount=length_of_stay_discount,
            length_of_stay_discount_percent=length_of_stay_discount_percent,
            cleaning_fee=cleaning_fee,
            pet_fee=pet_fee,
            other_fees=other_fees,
            taxes=taxes,
            total=total,
        )


        quote_pricing.additional_properties = d
        return quote_pricing

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
