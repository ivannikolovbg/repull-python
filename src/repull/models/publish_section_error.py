from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.publish_section_error_code import PublishSectionErrorCode
from ..models.publish_section_error_section import PublishSectionErrorSection
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PublishSectionError")



@_attrs_define
class PublishSectionError:
    """ One section of a publish that did not reach Airbnb.

        Attributes:
            section (PublishSectionErrorSection): Which part of the listing this failure is about.
            message (str): Airbnb's own reason, verbatim, or ours when we refused to send an empty section.
            code (PublishSectionErrorCode): `locked` — Airbnb refuses to change these fields on this listing; retrying
                cannot succeed and `lockedFields` names them. `no_content` — there was nothing canonical to send; write the
                content, then publish again. `rejected` — Airbnb refused the section as sent; fix the content and publish again.
            locked_fields (list[str] | Unset): For `code: locked` — the fields Airbnb dropped.
     """

    section: PublishSectionErrorSection
    message: str
    code: PublishSectionErrorCode
    locked_fields: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        section = self.section.value

        message = self.message

        code = self.code.value

        locked_fields: list[str] | Unset = UNSET
        if not isinstance(self.locked_fields, Unset):
            locked_fields = self.locked_fields




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "section": section,
            "message": message,
            "code": code,
        })
        if locked_fields is not UNSET:
            field_dict["lockedFields"] = locked_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        section = PublishSectionErrorSection(d.pop("section"))




        message = d.pop("message")

        code = PublishSectionErrorCode(d.pop("code"))




        locked_fields = cast(list[str], d.pop("lockedFields", UNSET))


        publish_section_error = cls(
            section=section,
            message=message,
            code=code,
            locked_fields=locked_fields,
        )


        publish_section_error.additional_properties = d
        return publish_section_error

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
