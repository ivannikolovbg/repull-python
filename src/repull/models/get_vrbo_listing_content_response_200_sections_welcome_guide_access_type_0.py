from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0")



@_attrs_define
class GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0:
    """ 
        Attributes:
            type_ (None | str | Unset):
            code (None | str | Unset):
            instructions (None | str | Unset):
     """

    type_: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    instructions: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        get_vrbo_listing_content_response_200_sections_welcome_guide_access_type_0 = cls(
            type_=type_,
            code=code,
            instructions=instructions,
        )


        get_vrbo_listing_content_response_200_sections_welcome_guide_access_type_0.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_welcome_guide_access_type_0

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
