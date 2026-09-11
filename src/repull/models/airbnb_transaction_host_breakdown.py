from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbTransactionHostBreakdown")



@_attrs_define
class AirbnbTransactionHostBreakdown:
    """ Host-side breakdown (all host currency).

        Attributes:
            host_payout (float | None): Expected/actual net payout to the host.
            accommodation_subtotal (float | None | Unset): Nightly rate × nights, net of stay-level discounts already
                applied by Airbnb.
            cleaning_fee (float | None | Unset):
            host_service_fee_base (float | None | Unset): Airbnb host service fee, base component (negative = deduction).
            host_service_fee_vat (float | None | Unset): Airbnb host service fee, VAT component (negative = deduction).
            host_service_fee_total (float | None | Unset): Convenience sum of base + VAT.
            airbnb_collected_tax (float | None | Unset):
            pass_through_tax (float | None | Unset):
            occupancy_tax (float | None | Unset):
            tax_withholding (float | None | Unset):
     """

    host_payout: float | None
    accommodation_subtotal: float | None | Unset = UNSET
    cleaning_fee: float | None | Unset = UNSET
    host_service_fee_base: float | None | Unset = UNSET
    host_service_fee_vat: float | None | Unset = UNSET
    host_service_fee_total: float | None | Unset = UNSET
    airbnb_collected_tax: float | None | Unset = UNSET
    pass_through_tax: float | None | Unset = UNSET
    occupancy_tax: float | None | Unset = UNSET
    tax_withholding: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        host_payout: float | None
        host_payout = self.host_payout

        accommodation_subtotal: float | None | Unset
        if isinstance(self.accommodation_subtotal, Unset):
            accommodation_subtotal = UNSET
        else:
            accommodation_subtotal = self.accommodation_subtotal

        cleaning_fee: float | None | Unset
        if isinstance(self.cleaning_fee, Unset):
            cleaning_fee = UNSET
        else:
            cleaning_fee = self.cleaning_fee

        host_service_fee_base: float | None | Unset
        if isinstance(self.host_service_fee_base, Unset):
            host_service_fee_base = UNSET
        else:
            host_service_fee_base = self.host_service_fee_base

        host_service_fee_vat: float | None | Unset
        if isinstance(self.host_service_fee_vat, Unset):
            host_service_fee_vat = UNSET
        else:
            host_service_fee_vat = self.host_service_fee_vat

        host_service_fee_total: float | None | Unset
        if isinstance(self.host_service_fee_total, Unset):
            host_service_fee_total = UNSET
        else:
            host_service_fee_total = self.host_service_fee_total

        airbnb_collected_tax: float | None | Unset
        if isinstance(self.airbnb_collected_tax, Unset):
            airbnb_collected_tax = UNSET
        else:
            airbnb_collected_tax = self.airbnb_collected_tax

        pass_through_tax: float | None | Unset
        if isinstance(self.pass_through_tax, Unset):
            pass_through_tax = UNSET
        else:
            pass_through_tax = self.pass_through_tax

        occupancy_tax: float | None | Unset
        if isinstance(self.occupancy_tax, Unset):
            occupancy_tax = UNSET
        else:
            occupancy_tax = self.occupancy_tax

        tax_withholding: float | None | Unset
        if isinstance(self.tax_withholding, Unset):
            tax_withholding = UNSET
        else:
            tax_withholding = self.tax_withholding


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "host_payout": host_payout,
        })
        if accommodation_subtotal is not UNSET:
            field_dict["accommodation_subtotal"] = accommodation_subtotal
        if cleaning_fee is not UNSET:
            field_dict["cleaning_fee"] = cleaning_fee
        if host_service_fee_base is not UNSET:
            field_dict["host_service_fee_base"] = host_service_fee_base
        if host_service_fee_vat is not UNSET:
            field_dict["host_service_fee_vat"] = host_service_fee_vat
        if host_service_fee_total is not UNSET:
            field_dict["host_service_fee_total"] = host_service_fee_total
        if airbnb_collected_tax is not UNSET:
            field_dict["airbnb_collected_tax"] = airbnb_collected_tax
        if pass_through_tax is not UNSET:
            field_dict["pass_through_tax"] = pass_through_tax
        if occupancy_tax is not UNSET:
            field_dict["occupancy_tax"] = occupancy_tax
        if tax_withholding is not UNSET:
            field_dict["tax_withholding"] = tax_withholding

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_host_payout(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        host_payout = _parse_host_payout(d.pop("host_payout"))


        def _parse_accommodation_subtotal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        accommodation_subtotal = _parse_accommodation_subtotal(d.pop("accommodation_subtotal", UNSET))


        def _parse_cleaning_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cleaning_fee = _parse_cleaning_fee(d.pop("cleaning_fee", UNSET))


        def _parse_host_service_fee_base(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        host_service_fee_base = _parse_host_service_fee_base(d.pop("host_service_fee_base", UNSET))


        def _parse_host_service_fee_vat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        host_service_fee_vat = _parse_host_service_fee_vat(d.pop("host_service_fee_vat", UNSET))


        def _parse_host_service_fee_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        host_service_fee_total = _parse_host_service_fee_total(d.pop("host_service_fee_total", UNSET))


        def _parse_airbnb_collected_tax(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        airbnb_collected_tax = _parse_airbnb_collected_tax(d.pop("airbnb_collected_tax", UNSET))


        def _parse_pass_through_tax(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pass_through_tax = _parse_pass_through_tax(d.pop("pass_through_tax", UNSET))


        def _parse_occupancy_tax(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        occupancy_tax = _parse_occupancy_tax(d.pop("occupancy_tax", UNSET))


        def _parse_tax_withholding(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tax_withholding = _parse_tax_withholding(d.pop("tax_withholding", UNSET))


        airbnb_transaction_host_breakdown = cls(
            host_payout=host_payout,
            accommodation_subtotal=accommodation_subtotal,
            cleaning_fee=cleaning_fee,
            host_service_fee_base=host_service_fee_base,
            host_service_fee_vat=host_service_fee_vat,
            host_service_fee_total=host_service_fee_total,
            airbnb_collected_tax=airbnb_collected_tax,
            pass_through_tax=pass_through_tax,
            occupancy_tax=occupancy_tax,
            tax_withholding=tax_withholding,
        )


        airbnb_transaction_host_breakdown.additional_properties = d
        return airbnb_transaction_host_breakdown

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
