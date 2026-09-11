from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_money_line import ReservationMoneyLine





T = TypeVar("T", bound="ReservationGuestFinancials")



@_attrs_define
class ReservationGuestFinancials:
    """ GUEST-side view of the stay — what the guest was actually charged. Same non-fabrication rule as
    `ReservationHostFinancials`: absent components are omitted, never zero-filled.

        Attributes:
            total_price (float | Unset): Stay total the guest paid, in `currency`. Taken from the stored breakdown; falls
                back to the reservation total when the breakdown carries no total of its own. Example: 739.32.
            fees (list[ReservationMoneyLine] | Unset): Every fee line the guest was charged — cleaning, extra guest, pass-
                through host fees, platform guest service fee, channel add-ons. Deduplicated: channels that report a fee both as
                an array line and as a scalar (e.g. `cleaning`) yield ONE line.
            taxes (list[ReservationMoneyLine] | Unset): Every tax line the guest was charged. Same collection as
                `financials.host.taxes`.
     """

    total_price: float | Unset = UNSET
    fees: list[ReservationMoneyLine] | Unset = UNSET
    taxes: list[ReservationMoneyLine] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_money_line import ReservationMoneyLine
        total_price = self.total_price

        fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)



        taxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if fees is not UNSET:
            field_dict["fees"] = fees
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_money_line import ReservationMoneyLine
        d = dict(src_dict)
        total_price = d.pop("totalPrice", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: list[ReservationMoneyLine] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = ReservationMoneyLine.from_dict(fees_item_data)



                fees.append(fees_item)


        _taxes = d.pop("taxes", UNSET)
        taxes: list[ReservationMoneyLine] | Unset = UNSET
        if _taxes is not UNSET:
            taxes = []
            for taxes_item_data in _taxes:
                taxes_item = ReservationMoneyLine.from_dict(taxes_item_data)



                taxes.append(taxes_item)


        reservation_guest_financials = cls(
            total_price=total_price,
            fees=fees,
            taxes=taxes,
        )


        reservation_guest_financials.additional_properties = d
        return reservation_guest_financials

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
