from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TransactionFees")



@_attrs_define
class TransactionFees:
    """ 
        Attributes:
            commission (float | None): Channel commission deducted. Example: 3340.8.
            service_fee (float | None): Payments service fee deducted. Example: 334.08.
            processing_fee (float | None):
     """

    commission: float | None
    service_fee: float | None
    processing_fee: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        commission: float | None
        commission = self.commission

        service_fee: float | None
        service_fee = self.service_fee

        processing_fee: float | None
        processing_fee = self.processing_fee


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "commission": commission,
            "serviceFee": service_fee,
            "processingFee": processing_fee,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_commission(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        commission = _parse_commission(d.pop("commission"))


        def _parse_service_fee(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        service_fee = _parse_service_fee(d.pop("serviceFee"))


        def _parse_processing_fee(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        processing_fee = _parse_processing_fee(d.pop("processingFee"))


        transaction_fees = cls(
            commission=commission,
            service_fee=service_fee,
            processing_fee=processing_fee,
        )


        transaction_fees.additional_properties = d
        return transaction_fees

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
