from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingHouseRulesBodyChildrenAgesItem")



@_attrs_define
class UpdateVrboListingHouseRulesBodyChildrenAgesItem:
    """ 
        Attributes:
            min_ (int | Unset):
            max_ (int | Unset):
     """

    min_: int | Unset = UNSET
    max_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_ = self.max_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        update_vrbo_listing_house_rules_body_children_ages_item = cls(
            min_=min_,
            max_=max_,
        )


        update_vrbo_listing_house_rules_body_children_ages_item.additional_properties = d
        return update_vrbo_listing_house_rules_body_children_ages_item

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
