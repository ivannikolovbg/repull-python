from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReservationQuoteResponseBreakdownType0")



@_attrs_define
class ReservationQuoteResponseBreakdownType0:
    """ The parts the PMS itemized; absent parts were not itemized.

        Attributes:
            accommodation (float | Unset):
            cleaning_fee (float | Unset):
            taxes (float | Unset):
            fees (float | Unset):
     """

    accommodation: float | Unset = UNSET
    cleaning_fee: float | Unset = UNSET
    taxes: float | Unset = UNSET
    fees: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        accommodation = self.accommodation

        cleaning_fee = self.cleaning_fee

        taxes = self.taxes

        fees = self.fees


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if accommodation is not UNSET:
            field_dict["accommodation"] = accommodation
        if cleaning_fee is not UNSET:
            field_dict["cleaningFee"] = cleaning_fee
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if fees is not UNSET:
            field_dict["fees"] = fees

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accommodation = d.pop("accommodation", UNSET)

        cleaning_fee = d.pop("cleaningFee", UNSET)

        taxes = d.pop("taxes", UNSET)

        fees = d.pop("fees", UNSET)

        reservation_quote_response_breakdown_type_0 = cls(
            accommodation=accommodation,
            cleaning_fee=cleaning_fee,
            taxes=taxes,
            fees=fees,
        )


        reservation_quote_response_breakdown_type_0.additional_properties = d
        return reservation_quote_response_breakdown_type_0

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
