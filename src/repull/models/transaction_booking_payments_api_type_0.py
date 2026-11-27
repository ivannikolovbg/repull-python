from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transaction_booking_payments_api_type_0_source import TransactionBookingPaymentsApiType0Source
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.transaction_booking_payments_api_type_0_bank_transfer_type_0 import TransactionBookingPaymentsApiType0BankTransferType0
  from ..models.transaction_booking_payments_api_type_0_charges_item import TransactionBookingPaymentsApiType0ChargesItem





T = TypeVar("T", bound="TransactionBookingPaymentsApiType0")



@_attrs_define
class TransactionBookingPaymentsApiType0:
    """ Booking.com only: the booking's payout and price breakdown as Booking.com's Payments API reports it (read when
    Booking.com notifies a payout change). Null on other channels and for bookings not read yet. Money is in `currency`.

        Attributes:
            source (TransactionBookingPaymentsApiType0Source | Unset):
            payment_tags (list[str] | Unset): `PAYMENTS_BY_BOOKING`, `PAYMENT_AT_PROPERTY` or `SMART_PAYMENT_AT_PROPERTY`.
                Example: ['PAYMENTS_BY_BOOKING'].
            payout_type (None | str | Unset): `GROSS`, `NET` or `UNKNOWN`; null when the property collects the payment.
                Example: NET.
            payout_status (None | str | Unset): `PENDING`, `PAID`, `CANCELLED` or `UNKNOWN`. Example: PAID.
            currency (None | str | Unset):  Example: EUR.
            gross_amount (float | None | Unset): What the guest paid Booking.com. Example: 120.
            commission (float | None | Unset):  Example: 18.
            payment_charge (float | None | Unset): Payments service charge. Example: 2.
            vat (float | None | Unset):  Example: 10.
            vat_on_fees (float | None | Unset): VAT on commission and on the payment charge. Example: 2.
            taxes (float | None | Unset): City tax, withheld and other taxes. Example: 6.26.
            net_amount (float | None | Unset): Estimated payout to the property. Example: 96.74.
            amount_to_collect_at_property (float | None | Unset): Estimated amount the property collects itself (e.g. city
                tax, or the whole stay when the property collects the payment). Example: 5.
            bank_transfer (None | TransactionBookingPaymentsApiType0BankTransferType0 | Unset):
            charges (list[TransactionBookingPaymentsApiType0ChargesItem] | Unset): Per-room price lines as Booking.com
                reports them.
            fetched_at (datetime.datetime | None | Unset):
     """

    source: TransactionBookingPaymentsApiType0Source | Unset = UNSET
    payment_tags: list[str] | Unset = UNSET
    payout_type: None | str | Unset = UNSET
    payout_status: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    gross_amount: float | None | Unset = UNSET
    commission: float | None | Unset = UNSET
    payment_charge: float | None | Unset = UNSET
    vat: float | None | Unset = UNSET
    vat_on_fees: float | None | Unset = UNSET
    taxes: float | None | Unset = UNSET
    net_amount: float | None | Unset = UNSET
    amount_to_collect_at_property: float | None | Unset = UNSET
    bank_transfer: None | TransactionBookingPaymentsApiType0BankTransferType0 | Unset = UNSET
    charges: list[TransactionBookingPaymentsApiType0ChargesItem] | Unset = UNSET
    fetched_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_booking_payments_api_type_0_bank_transfer_type_0 import TransactionBookingPaymentsApiType0BankTransferType0
        from ..models.transaction_booking_payments_api_type_0_charges_item import TransactionBookingPaymentsApiType0ChargesItem
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        payment_tags: list[str] | Unset = UNSET
        if not isinstance(self.payment_tags, Unset):
            payment_tags = self.payment_tags



        payout_type: None | str | Unset
        if isinstance(self.payout_type, Unset):
            payout_type = UNSET
        else:
            payout_type = self.payout_type

        payout_status: None | str | Unset
        if isinstance(self.payout_status, Unset):
            payout_status = UNSET
        else:
            payout_status = self.payout_status

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        gross_amount: float | None | Unset
        if isinstance(self.gross_amount, Unset):
            gross_amount = UNSET
        else:
            gross_amount = self.gross_amount

        commission: float | None | Unset
        if isinstance(self.commission, Unset):
            commission = UNSET
        else:
            commission = self.commission

        payment_charge: float | None | Unset
        if isinstance(self.payment_charge, Unset):
            payment_charge = UNSET
        else:
            payment_charge = self.payment_charge

        vat: float | None | Unset
        if isinstance(self.vat, Unset):
            vat = UNSET
        else:
            vat = self.vat

        vat_on_fees: float | None | Unset
        if isinstance(self.vat_on_fees, Unset):
            vat_on_fees = UNSET
        else:
            vat_on_fees = self.vat_on_fees

        taxes: float | None | Unset
        if isinstance(self.taxes, Unset):
            taxes = UNSET
        else:
            taxes = self.taxes

        net_amount: float | None | Unset
        if isinstance(self.net_amount, Unset):
            net_amount = UNSET
        else:
            net_amount = self.net_amount

        amount_to_collect_at_property: float | None | Unset
        if isinstance(self.amount_to_collect_at_property, Unset):
            amount_to_collect_at_property = UNSET
        else:
            amount_to_collect_at_property = self.amount_to_collect_at_property

        bank_transfer: dict[str, Any] | None | Unset
        if isinstance(self.bank_transfer, Unset):
            bank_transfer = UNSET
        elif isinstance(self.bank_transfer, TransactionBookingPaymentsApiType0BankTransferType0):
            bank_transfer = self.bank_transfer.to_dict()
        else:
            bank_transfer = self.bank_transfer

        charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)



        fetched_at: None | str | Unset
        if isinstance(self.fetched_at, Unset):
            fetched_at = UNSET
        elif isinstance(self.fetched_at, datetime.datetime):
            fetched_at = self.fetched_at.isoformat()
        else:
            fetched_at = self.fetched_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if payment_tags is not UNSET:
            field_dict["paymentTags"] = payment_tags
        if payout_type is not UNSET:
            field_dict["payoutType"] = payout_type
        if payout_status is not UNSET:
            field_dict["payoutStatus"] = payout_status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if gross_amount is not UNSET:
            field_dict["grossAmount"] = gross_amount
        if commission is not UNSET:
            field_dict["commission"] = commission
        if payment_charge is not UNSET:
            field_dict["paymentCharge"] = payment_charge
        if vat is not UNSET:
            field_dict["vat"] = vat
        if vat_on_fees is not UNSET:
            field_dict["vatOnFees"] = vat_on_fees
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if amount_to_collect_at_property is not UNSET:
            field_dict["amountToCollectAtProperty"] = amount_to_collect_at_property
        if bank_transfer is not UNSET:
            field_dict["bankTransfer"] = bank_transfer
        if charges is not UNSET:
            field_dict["charges"] = charges
        if fetched_at is not UNSET:
            field_dict["fetchedAt"] = fetched_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_booking_payments_api_type_0_bank_transfer_type_0 import TransactionBookingPaymentsApiType0BankTransferType0
        from ..models.transaction_booking_payments_api_type_0_charges_item import TransactionBookingPaymentsApiType0ChargesItem
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: TransactionBookingPaymentsApiType0Source | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = TransactionBookingPaymentsApiType0Source(_source)




        payment_tags = cast(list[str], d.pop("paymentTags", UNSET))


        def _parse_payout_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payout_type = _parse_payout_type(d.pop("payoutType", UNSET))


        def _parse_payout_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payout_status = _parse_payout_status(d.pop("payoutStatus", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_gross_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gross_amount = _parse_gross_amount(d.pop("grossAmount", UNSET))


        def _parse_commission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        commission = _parse_commission(d.pop("commission", UNSET))


        def _parse_payment_charge(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payment_charge = _parse_payment_charge(d.pop("paymentCharge", UNSET))


        def _parse_vat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vat = _parse_vat(d.pop("vat", UNSET))


        def _parse_vat_on_fees(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vat_on_fees = _parse_vat_on_fees(d.pop("vatOnFees", UNSET))


        def _parse_taxes(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        taxes = _parse_taxes(d.pop("taxes", UNSET))


        def _parse_net_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        net_amount = _parse_net_amount(d.pop("netAmount", UNSET))


        def _parse_amount_to_collect_at_property(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_to_collect_at_property = _parse_amount_to_collect_at_property(d.pop("amountToCollectAtProperty", UNSET))


        def _parse_bank_transfer(data: object) -> None | TransactionBookingPaymentsApiType0BankTransferType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bank_transfer_type_0 = TransactionBookingPaymentsApiType0BankTransferType0.from_dict(data)



                return bank_transfer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionBookingPaymentsApiType0BankTransferType0 | Unset, data)

        bank_transfer = _parse_bank_transfer(d.pop("bankTransfer", UNSET))


        _charges = d.pop("charges", UNSET)
        charges: list[TransactionBookingPaymentsApiType0ChargesItem] | Unset = UNSET
        if _charges is not UNSET:
            charges = []
            for charges_item_data in _charges:
                charges_item = TransactionBookingPaymentsApiType0ChargesItem.from_dict(charges_item_data)



                charges.append(charges_item)


        def _parse_fetched_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fetched_at_type_0 = isoparse(data)



                return fetched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fetched_at = _parse_fetched_at(d.pop("fetchedAt", UNSET))


        transaction_booking_payments_api_type_0 = cls(
            source=source,
            payment_tags=payment_tags,
            payout_type=payout_type,
            payout_status=payout_status,
            currency=currency,
            gross_amount=gross_amount,
            commission=commission,
            payment_charge=payment_charge,
            vat=vat,
            vat_on_fees=vat_on_fees,
            taxes=taxes,
            net_amount=net_amount,
            amount_to_collect_at_property=amount_to_collect_at_property,
            bank_transfer=bank_transfer,
            charges=charges,
            fetched_at=fetched_at,
        )


        transaction_booking_payments_api_type_0.additional_properties = d
        return transaction_booking_payments_api_type_0

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
