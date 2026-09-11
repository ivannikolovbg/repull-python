from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbTransactionPayout")



@_attrs_define
class AirbnbTransactionPayout:
    """ 
        Attributes:
            payout_id (None | str):
            payout_date (datetime.date | None): Settlement date (populated on Payout-type rows).
            paid_out_amount (float | None):
     """

    payout_id: None | str
    payout_date: datetime.date | None
    paid_out_amount: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payout_id: None | str
        payout_id = self.payout_id

        payout_date: None | str
        if isinstance(self.payout_date, datetime.date):
            payout_date = self.payout_date.isoformat()
        else:
            payout_date = self.payout_date

        paid_out_amount: float | None
        paid_out_amount = self.paid_out_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "payout_id": payout_id,
            "payout_date": payout_date,
            "paid_out_amount": paid_out_amount,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_payout_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payout_id = _parse_payout_id(d.pop("payout_id"))


        def _parse_payout_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payout_date_type_0 = isoparse(data).date()



                return payout_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        payout_date = _parse_payout_date(d.pop("payout_date"))


        def _parse_paid_out_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        paid_out_amount = _parse_paid_out_amount(d.pop("paid_out_amount"))


        airbnb_transaction_payout = cls(
            payout_id=payout_id,
            payout_date=payout_date,
            paid_out_amount=paid_out_amount,
        )


        airbnb_transaction_payout.additional_properties = d
        return airbnb_transaction_payout

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
