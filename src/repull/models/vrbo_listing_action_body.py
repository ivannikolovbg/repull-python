from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_listing_action_body_action import VrboListingActionBodyAction
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="VrboListingActionBody")



@_attrs_define
class VrboListingActionBody:
    """ 
        Attributes:
            action (VrboListingActionBodyAction):
            vrbo_listing_number (str | Unset): `push` / `unlist` / `relist`: the Vrbo listing, when the listing is linked to
                several.
            sections (list[str] | Unset): `push`: only these sections (as for `POST /v1/listings/{id}/publish/vrbo`).
     """

    action: VrboListingActionBodyAction
    vrbo_listing_number: str | Unset = UNSET
    sections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        vrbo_listing_number = self.vrbo_listing_number

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number
        if sections is not UNSET:
            field_dict["sections"] = sections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = VrboListingActionBodyAction(d.pop("action"))




        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        sections = cast(list[str], d.pop("sections", UNSET))


        vrbo_listing_action_body = cls(
            action=action,
            vrbo_listing_number=vrbo_listing_number,
            sections=sections,
        )


        vrbo_listing_action_body.additional_properties = d
        return vrbo_listing_action_body

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
