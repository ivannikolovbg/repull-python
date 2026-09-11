from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbTransactionGuestBreakdown")



@_attrs_define
class AirbnbTransactionGuestBreakdown:
    """ Guest-side breakdown (what the guest paid).

        Attributes:
            total_paid (float | None):
            service_fee_base (float | None | Unset):
            service_fee_vat (float | None | Unset):
     """

    total_paid: float | None
    service_fee_base: float | None | Unset = UNSET
    service_fee_vat: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_paid: float | None
        total_paid = self.total_paid

        service_fee_base: float | None | Unset
        if isinstance(self.service_fee_base, Unset):
            service_fee_base = UNSET
        else:
            service_fee_base = self.service_fee_base

        service_fee_vat: float | None | Unset
        if isinstance(self.service_fee_vat, Unset):
            service_fee_vat = UNSET
        else:
            service_fee_vat = self.service_fee_vat


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_paid": total_paid,
        })
        if service_fee_base is not UNSET:
            field_dict["service_fee_base"] = service_fee_base
        if service_fee_vat is not UNSET:
            field_dict["service_fee_vat"] = service_fee_vat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_total_paid(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        total_paid = _parse_total_paid(d.pop("total_paid"))


        def _parse_service_fee_base(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        service_fee_base = _parse_service_fee_base(d.pop("service_fee_base", UNSET))


        def _parse_service_fee_vat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        service_fee_vat = _parse_service_fee_vat(d.pop("service_fee_vat", UNSET))


        airbnb_transaction_guest_breakdown = cls(
            total_paid=total_paid,
            service_fee_base=service_fee_base,
            service_fee_vat=service_fee_vat,
        )


        airbnb_transaction_guest_breakdown.additional_properties = d
        return airbnb_transaction_guest_breakdown

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
