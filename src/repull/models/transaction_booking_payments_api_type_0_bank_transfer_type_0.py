from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TransactionBookingPaymentsApiType0BankTransferType0")



@_attrs_define
class TransactionBookingPaymentsApiType0BankTransferType0:
    """ 
        Attributes:
            reference (None | str | Unset): Booking.com bank-transfer reference; matches the payout on your bank statement.
                Example: ST-D0L8H1W4W9I5.
            status (None | str | Unset):  Example: PAID.
            date (None | str | Unset):  Example: 2026-05-04.
     """

    reference: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reference is not UNSET:
            field_dict["reference"] = reference
        if status is not UNSET:
            field_dict["status"] = status
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        transaction_booking_payments_api_type_0_bank_transfer_type_0 = cls(
            reference=reference,
            status=status,
            date=date,
        )


        transaction_booking_payments_api_type_0_bank_transfer_type_0.additional_properties = d
        return transaction_booking_payments_api_type_0_bank_transfer_type_0

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
