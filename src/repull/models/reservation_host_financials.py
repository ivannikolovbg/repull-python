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





T = TypeVar("T", bound="ReservationHostFinancials")



@_attrs_define
class ReservationHostFinancials:
    """ HOST-side view of the stay — what it looks like on the host ledger. Projected from the reservation's own stored
    price breakdown, so it is available on every channel (Airbnb, Booking.com, VRBO, direct, owner), not just Airbnb.

    **Nothing here is synthesised.** A property is present only when the source breakdown genuinely carries it; a
    component the channel never reported is OMITTED rather than returned as `0`. An empty array means the channel
    reported an empty collection.

        Attributes:
            accommodation (float | Unset): Accommodation subtotal before fees, taxes and discounts. Example: 485.
            discounts (list[ReservationMoneyLine] | Unset): Discounts applied to the stay (length-of-stay, non-refundable,
                promotional). Amounts are positive magnitudes of the reduction.
            guest_fees (list[ReservationMoneyLine] | Unset): The guest-side platform service fee as it appears on the host
                statement. Present only on channels that report it (Airbnb).
            host_fees (list[ReservationMoneyLine] | Unset): Fees the channel charged the HOST — host service fee /
                commission (with `vat` split out where the channel provides it), platform fee, payment processing fee.
            taxes (list[ReservationMoneyLine] | Unset): Taxes on the stay. Same collection as `financials.guest.taxes` —
                each line's `type` says who remits (`airbnb_collected` = the channel already collected and remitted it,
                `pass_through` = it reaches the host). The API deliberately does not split the list by remitter, so no
                classification of ours is baked into the payload.
            revenue (float | Unset): Expected host payout for the stay, in `currency`. Example: 566.72.
     """

    accommodation: float | Unset = UNSET
    discounts: list[ReservationMoneyLine] | Unset = UNSET
    guest_fees: list[ReservationMoneyLine] | Unset = UNSET
    host_fees: list[ReservationMoneyLine] | Unset = UNSET
    taxes: list[ReservationMoneyLine] | Unset = UNSET
    revenue: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_money_line import ReservationMoneyLine
        accommodation = self.accommodation

        discounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)



        guest_fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.guest_fees, Unset):
            guest_fees = []
            for guest_fees_item_data in self.guest_fees:
                guest_fees_item = guest_fees_item_data.to_dict()
                guest_fees.append(guest_fees_item)



        host_fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.host_fees, Unset):
            host_fees = []
            for host_fees_item_data in self.host_fees:
                host_fees_item = host_fees_item_data.to_dict()
                host_fees.append(host_fees_item)



        taxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)



        revenue = self.revenue


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if accommodation is not UNSET:
            field_dict["accommodation"] = accommodation
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if guest_fees is not UNSET:
            field_dict["guestFees"] = guest_fees
        if host_fees is not UNSET:
            field_dict["hostFees"] = host_fees
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if revenue is not UNSET:
            field_dict["revenue"] = revenue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_money_line import ReservationMoneyLine
        d = dict(src_dict)
        accommodation = d.pop("accommodation", UNSET)

        _discounts = d.pop("discounts", UNSET)
        discounts: list[ReservationMoneyLine] | Unset = UNSET
        if _discounts is not UNSET:
            discounts = []
            for discounts_item_data in _discounts:
                discounts_item = ReservationMoneyLine.from_dict(discounts_item_data)



                discounts.append(discounts_item)


        _guest_fees = d.pop("guestFees", UNSET)
        guest_fees: list[ReservationMoneyLine] | Unset = UNSET
        if _guest_fees is not UNSET:
            guest_fees = []
            for guest_fees_item_data in _guest_fees:
                guest_fees_item = ReservationMoneyLine.from_dict(guest_fees_item_data)



                guest_fees.append(guest_fees_item)


        _host_fees = d.pop("hostFees", UNSET)
        host_fees: list[ReservationMoneyLine] | Unset = UNSET
        if _host_fees is not UNSET:
            host_fees = []
            for host_fees_item_data in _host_fees:
                host_fees_item = ReservationMoneyLine.from_dict(host_fees_item_data)



                host_fees.append(host_fees_item)


        _taxes = d.pop("taxes", UNSET)
        taxes: list[ReservationMoneyLine] | Unset = UNSET
        if _taxes is not UNSET:
            taxes = []
            for taxes_item_data in _taxes:
                taxes_item = ReservationMoneyLine.from_dict(taxes_item_data)



                taxes.append(taxes_item)


        revenue = d.pop("revenue", UNSET)

        reservation_host_financials = cls(
            accommodation=accommodation,
            discounts=discounts,
            guest_fees=guest_fees,
            host_fees=host_fees,
            taxes=taxes,
            revenue=revenue,
        )


        reservation_host_financials.additional_properties = d
        return reservation_host_financials

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
