from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateVrboListingPaymentTermsBodyPaymentsItem")



@_attrs_define
class UpdateVrboListingPaymentTermsBodyPaymentsItem:
    """ 
        Attributes:
            percent (float):
            days_before_arrival (int):
     """

    percent: float
    days_before_arrival: int





    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        days_before_arrival = self.days_before_arrival


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "percent": percent,
            "daysBeforeArrival": days_before_arrival,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent")

        days_before_arrival = d.pop("daysBeforeArrival")

        update_vrbo_listing_payment_terms_body_payments_item = cls(
            percent=percent,
            days_before_arrival=days_before_arrival,
        )

        return update_vrbo_listing_payment_terms_body_payments_item

