from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingStoryBody")



@_attrs_define
class UpdateVrboListingStoryBody:
    """ 
        Attributes:
            about_you (str | Unset):
            why_this_property (str | Unset):
            unique_benefits (str | Unset):
     """

    about_you: str | Unset = UNSET
    why_this_property: str | Unset = UNSET
    unique_benefits: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        about_you = self.about_you

        why_this_property = self.why_this_property

        unique_benefits = self.unique_benefits


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if about_you is not UNSET:
            field_dict["aboutYou"] = about_you
        if why_this_property is not UNSET:
            field_dict["whyThisProperty"] = why_this_property
        if unique_benefits is not UNSET:
            field_dict["uniqueBenefits"] = unique_benefits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        about_you = d.pop("aboutYou", UNSET)

        why_this_property = d.pop("whyThisProperty", UNSET)

        unique_benefits = d.pop("uniqueBenefits", UNSET)

        update_vrbo_listing_story_body = cls(
            about_you=about_you,
            why_this_property=why_this_property,
            unique_benefits=unique_benefits,
        )

        return update_vrbo_listing_story_body

