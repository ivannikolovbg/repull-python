from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ErrorError")



@_attrs_define
class ErrorError:
    """ 
        Attributes:
            code (str | Unset):  Example: invalid_api_key.
            message (str | Unset):  Example: The API key provided is invalid..
            docs_url (str | Unset):  Example: https://repull.dev/docs/errors#invalid_api_key.
            example (str | Unset): Example of correct usage
     """

    code: str | Unset = UNSET
    message: str | Unset = UNSET
    docs_url: str | Unset = UNSET
    example: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        docs_url = self.docs_url

        example = self.example


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if docs_url is not UNSET:
            field_dict["docs_url"] = docs_url
        if example is not UNSET:
            field_dict["example"] = example

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        docs_url = d.pop("docs_url", UNSET)

        example = d.pop("example", UNSET)

        error_error = cls(
            code=code,
            message=message,
            docs_url=docs_url,
            example=example,
        )


        error_error.additional_properties = d
        return error_error

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
