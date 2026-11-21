from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingCheckinGuideBodyAccess")



@_attrs_define
class UpdateVrboListingCheckinGuideBodyAccess:
    """ 
        Attributes:
            type_ (str | Unset):
            code (str | Unset):
            instructions (str | Unset):
     """

    type_: str | Unset = UNSET
    code: str | Unset = UNSET
    instructions: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        code = self.code

        instructions = self.instructions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if code is not UNSET:
            field_dict["code"] = code
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        code = d.pop("code", UNSET)

        instructions = d.pop("instructions", UNSET)

        update_vrbo_listing_checkin_guide_body_access = cls(
            type_=type_,
            code=code,
            instructions=instructions,
        )

        return update_vrbo_listing_checkin_guide_body_access

