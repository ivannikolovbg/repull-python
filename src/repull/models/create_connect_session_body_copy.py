from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateConnectSessionBodyCopy")



@_attrs_define
class CreateConnectSessionBodyCopy:
    """ Migrate only — your wording for the hosted pages. Anything you leave out uses Repull's localized migration copy.

        Attributes:
            title (str | Unset):
            subtitle (str | Unset):
            completed_title (str | Unset):
            completed_body (str | Unset):
     """

    title: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    completed_title: str | Unset = UNSET
    completed_body: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        completed_title = self.completed_title

        completed_body = self.completed_body


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if completed_title is not UNSET:
            field_dict["completedTitle"] = completed_title
        if completed_body is not UNSET:
            field_dict["completedBody"] = completed_body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        completed_title = d.pop("completedTitle", UNSET)

        completed_body = d.pop("completedBody", UNSET)

        create_connect_session_body_copy = cls(
            title=title,
            subtitle=subtitle,
            completed_title=completed_title,
            completed_body=completed_body,
        )

        return create_connect_session_body_copy

