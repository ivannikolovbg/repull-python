from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingCancellationResponse200DataTiersItem")



@_attrs_define
class UpdateVrboListingCancellationResponse200DataTiersItem:
    """ 
        Attributes:
            days_before (int | None | Unset):
            refund_percent (float | None | Unset):
            penalty_percent (float | None | Unset):
     """

    days_before: int | None | Unset = UNSET
    refund_percent: float | None | Unset = UNSET
    penalty_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        days_before: int | None | Unset
        if isinstance(self.days_before, Unset):
            days_before = UNSET
        else:
            days_before = self.days_before

        refund_percent: float | None | Unset
        if isinstance(self.refund_percent, Unset):
            refund_percent = UNSET
        else:
            refund_percent = self.refund_percent

        penalty_percent: float | None | Unset
        if isinstance(self.penalty_percent, Unset):
            penalty_percent = UNSET
        else:
            penalty_percent = self.penalty_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if days_before is not UNSET:
            field_dict["daysBefore"] = days_before
        if refund_percent is not UNSET:
            field_dict["refundPercent"] = refund_percent
        if penalty_percent is not UNSET:
            field_dict["penaltyPercent"] = penalty_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_days_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_before = _parse_days_before(d.pop("daysBefore", UNSET))


        def _parse_refund_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refund_percent = _parse_refund_percent(d.pop("refundPercent", UNSET))


        def _parse_penalty_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        penalty_percent = _parse_penalty_percent(d.pop("penaltyPercent", UNSET))


        update_vrbo_listing_cancellation_response_200_data_tiers_item = cls(
            days_before=days_before,
            refund_percent=refund_percent,
            penalty_percent=penalty_percent,
        )


        update_vrbo_listing_cancellation_response_200_data_tiers_item.additional_properties = d
        return update_vrbo_listing_cancellation_response_200_data_tiers_item

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
