from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_input_channel import PromotionInputChannel
from ..models.promotion_type import PromotionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_rules import PromotionRules





T = TypeVar("T", bound="PromotionInput")



@_attrs_define
class PromotionInput:
    """ 
        Attributes:
            channel (PromotionInputChannel):
            type_ (PromotionType): The same idea on both channels shares a type: `mobile` is Airbnb’s mobile-only discount
                or Booking.com’s mobile rate; `new_listing` is Airbnb’s new listing promotion or Booking.com’s new property
                deal. `top_rated_guests` is Airbnb only; the deal, last-minute, early-booker, country and campaign types are
                Booking.com only; `custom` (Airbnb Custom promotion) is read-only.
            name (str | Unset): Booking.com only; only you see it.
            discount_percent (int | Unset): Booking.com only — Airbnb sets its own rates. Limits per type are in the
                catalog.
            rules (PromotionRules | Unset): Which rules a type supports depends on the channel — see the catalog.
     """

    channel: PromotionInputChannel
    type_: PromotionType
    name: str | Unset = UNSET
    discount_percent: int | Unset = UNSET
    rules: PromotionRules | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_rules import PromotionRules
        channel = self.channel.value

        type_ = self.type_.value

        name = self.name

        discount_percent = self.discount_percent

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "type": type_,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_rules import PromotionRules
        d = dict(src_dict)
        channel = PromotionInputChannel(d.pop("channel"))




        type_ = PromotionType(d.pop("type"))




        name = d.pop("name", UNSET)

        discount_percent = d.pop("discountPercent", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: PromotionRules | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = PromotionRules.from_dict(_rules)




        promotion_input = cls(
            channel=channel,
            type_=type_,
            name=name,
            discount_percent=discount_percent,
            rules=rules,
        )


        promotion_input.additional_properties = d
        return promotion_input

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
