from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PromotionRulesBlackoutDatesQuota")



@_attrs_define
class PromotionRulesBlackoutDatesQuota:
    """ 
        Attributes:
            used (int | Unset):
            available (int | Unset):
     """

    used: int | Unset = UNSET
    available: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        used = self.used

        available = self.available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if used is not UNSET:
            field_dict["used"] = used
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used", UNSET)

        available = d.pop("available", UNSET)

        promotion_rules_blackout_dates_quota = cls(
            used=used,
            available=available,
        )


        promotion_rules_blackout_dates_quota.additional_properties = d
        return promotion_rules_blackout_dates_quota

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
