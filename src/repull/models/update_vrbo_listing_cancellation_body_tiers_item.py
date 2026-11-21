from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateVrboListingCancellationBodyTiersItem")



@_attrs_define
class UpdateVrboListingCancellationBodyTiersItem:
    """ 
        Attributes:
            days_before (int):
            refund_percent (float):
     """

    days_before: int
    refund_percent: float





    def to_dict(self) -> dict[str, Any]:
        days_before = self.days_before

        refund_percent = self.refund_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "daysBefore": days_before,
            "refundPercent": refund_percent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days_before = d.pop("daysBefore")

        refund_percent = d.pop("refundPercent")

        update_vrbo_listing_cancellation_body_tiers_item = cls(
            days_before=days_before,
            refund_percent=refund_percent,
        )

        return update_vrbo_listing_cancellation_body_tiers_item

