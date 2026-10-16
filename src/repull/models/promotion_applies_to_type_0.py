from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PromotionAppliesToType0")



@_attrs_define
class PromotionAppliesToType0:
    """ Booking.com only. An empty `rooms` list means every room on the property.

        Attributes:
            rooms (list[str] | Unset):
            rate_plans (list[str] | Unset):
     """

    rooms: list[str] | Unset = UNSET
    rate_plans: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rooms: list[str] | Unset = UNSET
        if not isinstance(self.rooms, Unset):
            rooms = self.rooms



        rate_plans: list[str] | Unset = UNSET
        if not isinstance(self.rate_plans, Unset):
            rate_plans = self.rate_plans




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if rate_plans is not UNSET:
            field_dict["ratePlans"] = rate_plans

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rooms = cast(list[str], d.pop("rooms", UNSET))


        rate_plans = cast(list[str], d.pop("ratePlans", UNSET))


        promotion_applies_to_type_0 = cls(
            rooms=rooms,
            rate_plans=rate_plans,
        )


        promotion_applies_to_type_0.additional_properties = d
        return promotion_applies_to_type_0

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
