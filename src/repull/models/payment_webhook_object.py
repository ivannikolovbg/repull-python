from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_webhook_object_transaction_type import PaymentWebhookObjectTransactionType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PaymentWebhookObject")



@_attrs_define
class PaymentWebhookObject:
    """ A money movement: a guest charge, a host payout, a refund, a tourist-tax pass-through, a resolution payout, or an
    adjustment that claws money back.

        Attributes:
            id (int):  Example: 277919.
            customer_id (int):  Example: 1.
            transaction_type (PaymentWebhookObjectTransactionType): Repull's normalised vocabulary for what this movement
                is. Example: payout.
            amount (str): Gross amount. Negative on adjustments and clawbacks — the sign is preserved so the direction never
                has to be inferred. Example: 1792.17.
            source_type (None | str | Unset): The source system's own type string, unmapped, for reconciling against the
                dashboard. Example: Payout.
            status (None | str | Unset):  Example: completed.
            currency (None | str | Unset):  Example: CAD.
            reservation_id (int | None | Unset): Present when the movement belongs to one reservation. Absent on batched
                payouts, which genuinely arrive without a reservation reference.
            confirmation_code (None | str | Unset): The channel's confirmation code, when resolved.
            listing_id (int | None | Unset):
            platform (None | str | Unset):  Example: airbnb.
            platform_payment_id (None | str | Unset): The platform's own id. Airbnb payout ids look like `G-FRSLYC3ZKAJDQ`.
                Example: G-FRSLYC3ZKAJDQ.
            processing_fee (None | str | Unset): Emitted only where the source carries it.
            net_amount (None | str | Unset): Emitted only where the source carries it.
     """

    id: int
    customer_id: int
    transaction_type: PaymentWebhookObjectTransactionType
    amount: str
    source_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    listing_id: int | None | Unset = UNSET
    platform: None | str | Unset = UNSET
    platform_payment_id: None | str | Unset = UNSET
    processing_fee: None | str | Unset = UNSET
    net_amount: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        transaction_type = self.transaction_type.value

        amount = self.amount

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        confirmation_code: None | str | Unset
        if isinstance(self.confirmation_code, Unset):
            confirmation_code = UNSET
        else:
            confirmation_code = self.confirmation_code

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        platform_payment_id: None | str | Unset
        if isinstance(self.platform_payment_id, Unset):
            platform_payment_id = UNSET
        else:
            platform_payment_id = self.platform_payment_id

        processing_fee: None | str | Unset
        if isinstance(self.processing_fee, Unset):
            processing_fee = UNSET
        else:
            processing_fee = self.processing_fee

        net_amount: None | str | Unset
        if isinstance(self.net_amount, Unset):
            net_amount = UNSET
        else:
            net_amount = self.net_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "transactionType": transaction_type,
            "amount": amount,
        })
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_payment_id is not UNSET:
            field_dict["platformPaymentId"] = platform_payment_id
        if processing_fee is not UNSET:
            field_dict["processingFee"] = processing_fee
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        transaction_type = PaymentWebhookObjectTransactionType(d.pop("transactionType"))




        amount = d.pop("amount")

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("sourceType", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmationCode", UNSET))


        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))


        def _parse_platform_payment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform_payment_id = _parse_platform_payment_id(d.pop("platformPaymentId", UNSET))


        def _parse_processing_fee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        processing_fee = _parse_processing_fee(d.pop("processingFee", UNSET))


        def _parse_net_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        net_amount = _parse_net_amount(d.pop("netAmount", UNSET))


        payment_webhook_object = cls(
            id=id,
            customer_id=customer_id,
            transaction_type=transaction_type,
            amount=amount,
            source_type=source_type,
            status=status,
            currency=currency,
            reservation_id=reservation_id,
            confirmation_code=confirmation_code,
            listing_id=listing_id,
            platform=platform,
            platform_payment_id=platform_payment_id,
            processing_fee=processing_fee,
            net_amount=net_amount,
        )


        payment_webhook_object.additional_properties = d
        return payment_webhook_object

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
