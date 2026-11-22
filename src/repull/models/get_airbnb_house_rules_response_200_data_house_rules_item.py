from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAirbnbHouseRulesResponse200DataHouseRulesItem")



@_attrs_define
class GetAirbnbHouseRulesResponse200DataHouseRulesItem:
    """ 
        Attributes:
            locale (None | str | Unset):
            text (None | str | Unset):
            additional_rules (Any | Unset):
     """

    locale: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    additional_rules: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        additional_rules = self.additional_rules


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if locale is not UNSET:
            field_dict["locale"] = locale
        if text is not UNSET:
            field_dict["text"] = text
        if additional_rules is not UNSET:
            field_dict["additionalRules"] = additional_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        additional_rules = d.pop("additionalRules", UNSET)

        get_airbnb_house_rules_response_200_data_house_rules_item = cls(
            locale=locale,
            text=text,
            additional_rules=additional_rules,
        )


        get_airbnb_house_rules_response_200_data_house_rules_item.additional_properties = d
        return get_airbnb_house_rules_response_200_data_house_rules_item

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
