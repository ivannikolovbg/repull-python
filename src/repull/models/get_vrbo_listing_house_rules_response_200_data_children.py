from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_house_rules_response_200_data_children_ages_item import GetVrboListingHouseRulesResponse200DataChildrenAgesItem





T = TypeVar("T", bound="GetVrboListingHouseRulesResponse200DataChildren")



@_attrs_define
class GetVrboListingHouseRulesResponse200DataChildren:
    """ 
        Attributes:
            allowed (bool | None | Unset):
            ages (list[GetVrboListingHouseRulesResponse200DataChildrenAgesItem] | Unset):
            note (None | str | Unset):
     """

    allowed: bool | None | Unset = UNSET
    ages: list[GetVrboListingHouseRulesResponse200DataChildrenAgesItem] | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_house_rules_response_200_data_children_ages_item import GetVrboListingHouseRulesResponse200DataChildrenAgesItem
        allowed: bool | None | Unset
        if isinstance(self.allowed, Unset):
            allowed = UNSET
        else:
            allowed = self.allowed

        ages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ages, Unset):
            ages = []
            for ages_item_data in self.ages:
                ages_item = ages_item_data.to_dict()
                ages.append(ages_item)



        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if ages is not UNSET:
            field_dict["ages"] = ages
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_house_rules_response_200_data_children_ages_item import GetVrboListingHouseRulesResponse200DataChildrenAgesItem
        d = dict(src_dict)
        def _parse_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allowed = _parse_allowed(d.pop("allowed", UNSET))


        _ages = d.pop("ages", UNSET)
        ages: list[GetVrboListingHouseRulesResponse200DataChildrenAgesItem] | Unset = UNSET
        if _ages is not UNSET:
            ages = []
            for ages_item_data in _ages:
                ages_item = GetVrboListingHouseRulesResponse200DataChildrenAgesItem.from_dict(ages_item_data)



                ages.append(ages_item)


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        get_vrbo_listing_house_rules_response_200_data_children = cls(
            allowed=allowed,
            ages=ages,
            note=note,
        )


        get_vrbo_listing_house_rules_response_200_data_children.additional_properties = d
        return get_vrbo_listing_house_rules_response_200_data_children

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
