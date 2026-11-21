from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_house_rules_body_children_ages_item import UpdateVrboListingHouseRulesBodyChildrenAgesItem





T = TypeVar("T", bound="UpdateVrboListingHouseRulesBodyChildren")



@_attrs_define
class UpdateVrboListingHouseRulesBodyChildren:
    """ 
        Attributes:
            allowed (bool | Unset):
            ages (list[UpdateVrboListingHouseRulesBodyChildrenAgesItem] | Unset):
            note (None | str | Unset):
     """

    allowed: bool | Unset = UNSET
    ages: list[UpdateVrboListingHouseRulesBodyChildrenAgesItem] | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_house_rules_body_children_ages_item import UpdateVrboListingHouseRulesBodyChildrenAgesItem
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
        from ..models.update_vrbo_listing_house_rules_body_children_ages_item import UpdateVrboListingHouseRulesBodyChildrenAgesItem
        d = dict(src_dict)
        allowed = d.pop("allowed", UNSET)

        _ages = d.pop("ages", UNSET)
        ages: list[UpdateVrboListingHouseRulesBodyChildrenAgesItem] | Unset = UNSET
        if _ages is not UNSET:
            ages = []
            for ages_item_data in _ages:
                ages_item = UpdateVrboListingHouseRulesBodyChildrenAgesItem.from_dict(ages_item_data)



                ages.append(ages_item)


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        update_vrbo_listing_house_rules_body_children = cls(
            allowed=allowed,
            ages=ages,
            note=note,
        )

        return update_vrbo_listing_house_rules_body_children

