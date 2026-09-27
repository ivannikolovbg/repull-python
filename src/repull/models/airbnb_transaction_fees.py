from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AirbnbTransactionFees")



@_attrs_define
class AirbnbTransactionFees:
    """ 
        Attributes:
            host_service_fee (float | None): Airbnb's host service fee on this line, as a deduction (negative). Already
                taken out of `amount`. Example: -7.45.
            cleaning_fee (float | None): Cleaning fee included in this line's gross. Example: 40.57.
     """

    host_service_fee: float | None
    cleaning_fee: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        host_service_fee: float | None
        host_service_fee = self.host_service_fee

        cleaning_fee: float | None
        cleaning_fee = self.cleaning_fee


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hostServiceFee": host_service_fee,
            "cleaningFee": cleaning_fee,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_host_service_fee(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        host_service_fee = _parse_host_service_fee(d.pop("hostServiceFee"))


        def _parse_cleaning_fee(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cleaning_fee = _parse_cleaning_fee(d.pop("cleaningFee"))


        airbnb_transaction_fees = cls(
            host_service_fee=host_service_fee,
            cleaning_fee=cleaning_fee,
        )


        airbnb_transaction_fees.additional_properties = d
        return airbnb_transaction_fees

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
