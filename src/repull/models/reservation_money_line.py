from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReservationMoneyLine")



@_attrs_define
class ReservationMoneyLine:
    """ One line inside a fee / tax / discount collection. `amount` is always a `number` in the reservation `currency` — the
    underlying channel data stores some amounts as decimal strings and the API coerces them. Every other property is
    passed through only when the source channel supplied it.

        Attributes:
            amount (float): Amount in the reservation `currency`. Example: 126.
            name (str | Unset): Label as the channel reported it. Example: Cleaning Fee.
            type_ (str | Unset): Channel-reported classifier. NOT an enum — new channels introduce new values. Observed on
                fees: `cleaning`, `extra_guest`, `service`, `guest_service`, `pet`, `fixed`, `add_on`, `host_service`,
                `platform`, `processing`. Observed on taxes: `airbnb_collected` (channel collected AND remitted it),
                `pass_through` (reaches the host to remit), `tax`, `custom`. Example: cleaning.
            description (str | Unset): Longer channel-supplied description. Only present when it differs from `name`.
                Example: Extra guest fee for 1 additional guest(s).
            quantity (float | Unset): Units billed, when the channel reports a quantity (Booking.com add-ons). Example: 1.
            vat (float | Unset): VAT charged on top of this line, when the channel splits it out separately.
     """

    amount: float
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    description: str | Unset = UNSET
    quantity: float | Unset = UNSET
    vat: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        name = self.name

        type_ = self.type_

        description = self.description

        quantity = self.quantity

        vat = self.vat


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amount": amount,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if vat is not UNSET:
            field_dict["vat"] = vat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        vat = d.pop("vat", UNSET)

        reservation_money_line = cls(
            amount=amount,
            name=name,
            type_=type_,
            description=description,
            quantity=quantity,
            vat=vat,
        )


        reservation_money_line.additional_properties = d
        return reservation_money_line

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
