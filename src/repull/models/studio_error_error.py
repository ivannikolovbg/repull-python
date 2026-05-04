from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StudioErrorError")



@_attrs_define
class StudioErrorError:
    """ 
        Attributes:
            code (str): Stable machine-readable error code (e.g. `bad_request`, `not_found`, `rate_limited`).
            message (str): Human-readable description of what went wrong.
            fix (str | Unset): Suggested next action for the caller (optional).
            docs_url (str | Unset): Link to the docs page that explains this error.
     """

    code: str
    message: str
    fix: str | Unset = UNSET
    docs_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        fix = self.fix

        docs_url = self.docs_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "message": message,
        })
        if fix is not UNSET:
            field_dict["fix"] = fix
        if docs_url is not UNSET:
            field_dict["docs_url"] = docs_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        fix = d.pop("fix", UNSET)

        docs_url = d.pop("docs_url", UNSET)

        studio_error_error = cls(
            code=code,
            message=message,
            fix=fix,
            docs_url=docs_url,
        )


        studio_error_error.additional_properties = d
        return studio_error_error

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
