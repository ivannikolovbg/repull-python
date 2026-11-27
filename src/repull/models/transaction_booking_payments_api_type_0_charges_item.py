from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transaction_booking_payments_api_type_0_charges_item_category import TransactionBookingPaymentsApiType0ChargesItemCategory
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.transaction_booking_payments_api_type_0_charges_item_rate_type_0 import TransactionBookingPaymentsApiType0ChargesItemRateType0





T = TypeVar("T", bound="TransactionBookingPaymentsApiType0ChargesItem")



@_attrs_define
class TransactionBookingPaymentsApiType0ChargesItem:
    """ 
        Attributes:
            type_ (str | Unset): Booking.com's label, e.g. `VAT`, `City tax`, `COMMISSION`, `PAYMENT CHARGE`. Example: VAT.
            category (TransactionBookingPaymentsApiType0ChargesItemCategory | Unset):
            amount (float | None | Unset):  Example: 10.
            currency (None | str | Unset):
            rate (None | TransactionBookingPaymentsApiType0ChargesItemRateType0 | Unset):
            applicable_type (None | str | Unset): e.g. `PER_PERSON`, `PER_NIGHT`.
            already_collected_from_guest (bool | None | Unset):
            included_in_payout (bool | None | Unset):
     """

    type_: str | Unset = UNSET
    category: TransactionBookingPaymentsApiType0ChargesItemCategory | Unset = UNSET
    amount: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    rate: None | TransactionBookingPaymentsApiType0ChargesItemRateType0 | Unset = UNSET
    applicable_type: None | str | Unset = UNSET
    already_collected_from_guest: bool | None | Unset = UNSET
    included_in_payout: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_booking_payments_api_type_0_charges_item_rate_type_0 import TransactionBookingPaymentsApiType0ChargesItemRateType0
        type_ = self.type_

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        rate: dict[str, Any] | None | Unset
        if isinstance(self.rate, Unset):
            rate = UNSET
        elif isinstance(self.rate, TransactionBookingPaymentsApiType0ChargesItemRateType0):
            rate = self.rate.to_dict()
        else:
            rate = self.rate

        applicable_type: None | str | Unset
        if isinstance(self.applicable_type, Unset):
            applicable_type = UNSET
        else:
            applicable_type = self.applicable_type

        already_collected_from_guest: bool | None | Unset
        if isinstance(self.already_collected_from_guest, Unset):
            already_collected_from_guest = UNSET
        else:
            already_collected_from_guest = self.already_collected_from_guest

        included_in_payout: bool | None | Unset
        if isinstance(self.included_in_payout, Unset):
            included_in_payout = UNSET
        else:
            included_in_payout = self.included_in_payout


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if category is not UNSET:
            field_dict["category"] = category
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if rate is not UNSET:
            field_dict["rate"] = rate
        if applicable_type is not UNSET:
            field_dict["applicableType"] = applicable_type
        if already_collected_from_guest is not UNSET:
            field_dict["alreadyCollectedFromGuest"] = already_collected_from_guest
        if included_in_payout is not UNSET:
            field_dict["includedInPayout"] = included_in_payout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_booking_payments_api_type_0_charges_item_rate_type_0 import TransactionBookingPaymentsApiType0ChargesItemRateType0
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _category = d.pop("category", UNSET)
        category: TransactionBookingPaymentsApiType0ChargesItemCategory | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = TransactionBookingPaymentsApiType0ChargesItemCategory(_category)




        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_rate(data: object) -> None | TransactionBookingPaymentsApiType0ChargesItemRateType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_type_0 = TransactionBookingPaymentsApiType0ChargesItemRateType0.from_dict(data)



                return rate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionBookingPaymentsApiType0ChargesItemRateType0 | Unset, data)

        rate = _parse_rate(d.pop("rate", UNSET))


        def _parse_applicable_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicable_type = _parse_applicable_type(d.pop("applicableType", UNSET))


        def _parse_already_collected_from_guest(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        already_collected_from_guest = _parse_already_collected_from_guest(d.pop("alreadyCollectedFromGuest", UNSET))


        def _parse_included_in_payout(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        included_in_payout = _parse_included_in_payout(d.pop("includedInPayout", UNSET))


        transaction_booking_payments_api_type_0_charges_item = cls(
            type_=type_,
            category=category,
            amount=amount,
            currency=currency,
            rate=rate,
            applicable_type=applicable_type,
            already_collected_from_guest=already_collected_from_guest,
            included_in_payout=included_in_payout,
        )


        transaction_booking_payments_api_type_0_charges_item.additional_properties = d
        return transaction_booking_payments_api_type_0_charges_item

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
