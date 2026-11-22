from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UpdateAirbnbHouseRulesBody")



@_attrs_define
class UpdateAirbnbHouseRulesBody:
    """ 
        Attributes:
            locale (str):  Example: en.
            house_rules (None | str):
     """

    locale: str
    house_rules: None | str





    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        house_rules: None | str
        house_rules = self.house_rules


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "locale": locale,
            "houseRules": house_rules,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        def _parse_house_rules(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        house_rules = _parse_house_rules(d.pop("houseRules"))


        update_airbnb_house_rules_body = cls(
            locale=locale,
            house_rules=house_rules,
        )

        return update_airbnb_house_rules_body

