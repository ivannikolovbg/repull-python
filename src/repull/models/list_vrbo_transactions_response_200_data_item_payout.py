from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ListVrboTransactionsResponse200DataItemPayout")



@_attrs_define
class ListVrboTransactionsResponse200DataItemPayout:
    """ 
        Attributes:
            payout_id (None | str | Unset):
            payout_date (datetime.date | None | Unset):
            line_index (int | None | Unset):
            paid_out_amount (float | None | Unset):
            bank_destination (None | str | Unset): The bank account, as Vrbo shows it (masked).
     """

    payout_id: None | str | Unset = UNSET
    payout_date: datetime.date | None | Unset = UNSET
    line_index: int | None | Unset = UNSET
    paid_out_amount: float | None | Unset = UNSET
    bank_destination: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payout_id: None | str | Unset
        if isinstance(self.payout_id, Unset):
            payout_id = UNSET
        else:
            payout_id = self.payout_id

        payout_date: None | str | Unset
        if isinstance(self.payout_date, Unset):
            payout_date = UNSET
        elif isinstance(self.payout_date, datetime.date):
            payout_date = self.payout_date.isoformat()
        else:
            payout_date = self.payout_date

        line_index: int | None | Unset
        if isinstance(self.line_index, Unset):
            line_index = UNSET
        else:
            line_index = self.line_index

        paid_out_amount: float | None | Unset
        if isinstance(self.paid_out_amount, Unset):
            paid_out_amount = UNSET
        else:
            paid_out_amount = self.paid_out_amount

        bank_destination: None | str | Unset
        if isinstance(self.bank_destination, Unset):
            bank_destination = UNSET
        else:
            bank_destination = self.bank_destination


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if payout_id is not UNSET:
            field_dict["payoutId"] = payout_id
        if payout_date is not UNSET:
            field_dict["payoutDate"] = payout_date
        if line_index is not UNSET:
            field_dict["lineIndex"] = line_index
        if paid_out_amount is not UNSET:
            field_dict["paidOutAmount"] = paid_out_amount
        if bank_destination is not UNSET:
            field_dict["bankDestination"] = bank_destination

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_payout_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payout_id = _parse_payout_id(d.pop("payoutId", UNSET))


        def _parse_payout_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payout_date_type_0 = isoparse(data).date()



                return payout_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        payout_date = _parse_payout_date(d.pop("payoutDate", UNSET))


        def _parse_line_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line_index = _parse_line_index(d.pop("lineIndex", UNSET))


        def _parse_paid_out_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        paid_out_amount = _parse_paid_out_amount(d.pop("paidOutAmount", UNSET))


        def _parse_bank_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_destination = _parse_bank_destination(d.pop("bankDestination", UNSET))


        list_vrbo_transactions_response_200_data_item_payout = cls(
            payout_id=payout_id,
            payout_date=payout_date,
            line_index=line_index,
            paid_out_amount=paid_out_amount,
            bank_destination=bank_destination,
        )


        list_vrbo_transactions_response_200_data_item_payout.additional_properties = d
        return list_vrbo_transactions_response_200_data_item_payout

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
