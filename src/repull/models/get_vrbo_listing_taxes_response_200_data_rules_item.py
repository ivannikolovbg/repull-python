from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingTaxesResponse200DataRulesItem")



@_attrs_define
class GetVrboListingTaxesResponse200DataRulesItem:
    """ 
        Attributes:
            jurisdiction (None | str | Unset):
            level (None | str | Unset):
            rate (Any | Unset):
            type_ (None | str | Unset):
            applies_to (None | str | Unset):
     """

    jurisdiction: None | str | Unset = UNSET
    level: None | str | Unset = UNSET
    rate: Any | Unset = UNSET
    type_: None | str | Unset = UNSET
    applies_to: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        jurisdiction: None | str | Unset
        if isinstance(self.jurisdiction, Unset):
            jurisdiction = UNSET
        else:
            jurisdiction = self.jurisdiction

        level: None | str | Unset
        if isinstance(self.level, Unset):
            level = UNSET
        else:
            level = self.level

        rate = self.rate

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        applies_to: None | str | Unset
        if isinstance(self.applies_to, Unset):
            applies_to = UNSET
        else:
            applies_to = self.applies_to


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if level is not UNSET:
            field_dict["level"] = level
        if rate is not UNSET:
            field_dict["rate"] = rate
        if type_ is not UNSET:
            field_dict["type"] = type_
        if applies_to is not UNSET:
            field_dict["appliesTo"] = applies_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_jurisdiction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jurisdiction = _parse_jurisdiction(d.pop("jurisdiction", UNSET))


        def _parse_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level = _parse_level(d.pop("level", UNSET))


        rate = d.pop("rate", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_applies_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applies_to = _parse_applies_to(d.pop("appliesTo", UNSET))


        get_vrbo_listing_taxes_response_200_data_rules_item = cls(
            jurisdiction=jurisdiction,
            level=level,
            rate=rate,
            type_=type_,
            applies_to=applies_to,
        )


        get_vrbo_listing_taxes_response_200_data_rules_item.additional_properties = d
        return get_vrbo_listing_taxes_response_200_data_rules_item

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
