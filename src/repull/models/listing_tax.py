from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.charge_per import ChargePer
from ..models.listing_tax_amount_type import ListingTaxAmountType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingTax")



@_attrs_define
class ListingTax:
    """ A tax charged to the guest. One shape for every channel and PMS.

        Attributes:
            type_ (str | Unset): `vat`, `vat_gst`, `city_tax`, `transient_occupancy_tax`, … Example: vat.
            name (None | str | Unset):  Example: VAT.
            amount (float | Unset):  Example: 20.
            amount_type (ListingTaxAmountType | Unset):
            charged_per (ChargePer | Unset): How often an amount is charged: once per stay, per night, per guest, or per
                guest per night.
            applies_to (list[str] | None | Unset): What it is charged on (`accommodation`, `cleaning`, other fee types).
                `null`: the whole stay.
            included (bool | Unset): Already included in the price rather than added on top.
            source (str | Unset): `airbnb` (host-remitted), `airbnb_collected` (Airbnb collects and remits), `guesty`, …
     """

    type_: str | Unset = UNSET
    name: None | str | Unset = UNSET
    amount: float | Unset = UNSET
    amount_type: ListingTaxAmountType | Unset = UNSET
    charged_per: ChargePer | Unset = UNSET
    applies_to: list[str] | None | Unset = UNSET
    included: bool | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        amount = self.amount

        amount_type: str | Unset = UNSET
        if not isinstance(self.amount_type, Unset):
            amount_type = self.amount_type.value


        charged_per: str | Unset = UNSET
        if not isinstance(self.charged_per, Unset):
            charged_per = self.charged_per.value


        applies_to: list[str] | None | Unset
        if isinstance(self.applies_to, Unset):
            applies_to = UNSET
        elif isinstance(self.applies_to, list):
            applies_to = self.applies_to


        else:
            applies_to = self.applies_to

        included = self.included

        source = self.source


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_type is not UNSET:
            field_dict["amountType"] = amount_type
        if charged_per is not UNSET:
            field_dict["chargedPer"] = charged_per
        if applies_to is not UNSET:
            field_dict["appliesTo"] = applies_to
        if included is not UNSET:
            field_dict["included"] = included
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        amount = d.pop("amount", UNSET)

        _amount_type = d.pop("amountType", UNSET)
        amount_type: ListingTaxAmountType | Unset
        if isinstance(_amount_type,  Unset):
            amount_type = UNSET
        else:
            amount_type = ListingTaxAmountType(_amount_type)




        _charged_per = d.pop("chargedPer", UNSET)
        charged_per: ChargePer | Unset
        if isinstance(_charged_per,  Unset):
            charged_per = UNSET
        else:
            charged_per = ChargePer(_charged_per)




        def _parse_applies_to(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applies_to_type_0 = cast(list[str], data)

                return applies_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        applies_to = _parse_applies_to(d.pop("appliesTo", UNSET))


        included = d.pop("included", UNSET)

        source = d.pop("source", UNSET)

        listing_tax = cls(
            type_=type_,
            name=name,
            amount=amount,
            amount_type=amount_type,
            charged_per=charged_per,
            applies_to=applies_to,
            included=included,
            source=source,
        )


        listing_tax.additional_properties = d
        return listing_tax

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
