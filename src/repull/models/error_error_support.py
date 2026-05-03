from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ErrorErrorSupport")



@_attrs_define
class ErrorErrorSupport:
    """ LAST-RESORT contact handle. Only set on errors that genuinely cannot be self-fixed (billing dispute, account-state
    corruption, OAuth partner intervention). Never fall back to support before trying `fix` and `docs_url`.

        Attributes:
            email (str | Unset):
            url (str | Unset):
            reference (str | Unset): Internal reference to quote when contacting support.
     """

    email: str | Unset = UNSET
    url: str | Unset = UNSET
    reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        url = self.url

        reference = self.reference


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if url is not UNSET:
            field_dict["url"] = url
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        url = d.pop("url", UNSET)

        reference = d.pop("reference", UNSET)

        error_error_support = cls(
            email=email,
            url=url,
            reference=reference,
        )


        error_error_support.additional_properties = d
        return error_error_support

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
