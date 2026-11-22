from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbListingCancellationBodyNonRefundable")



@_attrs_define
class UpdateAirbnbListingCancellationBodyNonRefundable:
    """ 
        Attributes:
            enabled (bool | None | Unset):
            discount_percent (int | None | Unset):
     """

    enabled: bool | None | Unset = UNSET
    discount_percent: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        discount_percent: int | None | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        def _parse_discount_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discountPercent", UNSET))


        update_airbnb_listing_cancellation_body_non_refundable = cls(
            enabled=enabled,
            discount_percent=discount_percent,
        )

        return update_airbnb_listing_cancellation_body_non_refundable

