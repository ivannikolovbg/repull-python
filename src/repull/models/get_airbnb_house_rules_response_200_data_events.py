from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAirbnbHouseRulesResponse200DataEvents")



@_attrs_define
class GetAirbnbHouseRulesResponse200DataEvents:
    """ 
        Attributes:
            allowed (bool | None | Unset):
     """

    allowed: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed: bool | None | Unset
        if isinstance(self.allowed, Unset):
            allowed = UNSET
        else:
            allowed = self.allowed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allowed = _parse_allowed(d.pop("allowed", UNSET))


        get_airbnb_house_rules_response_200_data_events = cls(
            allowed=allowed,
        )


        get_airbnb_house_rules_response_200_data_events.additional_properties = d
        return get_airbnb_house_rules_response_200_data_events

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
