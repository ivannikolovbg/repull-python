from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="StudioFile")



@_attrs_define
class StudioFile:
    """ A single source file inside a Studio project. Files are addressed by their relative `path`.

        Attributes:
            path (str | Unset): Project-relative path, e.g. `src/app/page.tsx`.
            content (str | Unset): UTF-8 file contents.
            sha256 (str | Unset): SHA-256 hex digest of the content — use it to detect drift before writing.
            size (int | Unset): Byte length of the content.
            updated_at (datetime.datetime | Unset):
     """

    path: str | Unset = UNSET
    content: str | Unset = UNSET
    sha256: str | Unset = UNSET
    size: int | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        sha256 = self.sha256

        size = self.size

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if path is not UNSET:
            field_dict["path"] = path
        if content is not UNSET:
            field_dict["content"] = content
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if size is not UNSET:
            field_dict["size"] = size
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        content = d.pop("content", UNSET)

        sha256 = d.pop("sha256", UNSET)

        size = d.pop("size", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        studio_file = cls(
            path=path,
            content=content,
            sha256=sha256,
            size=size,
            updated_at=updated_at,
        )


        studio_file.additional_properties = d
        return studio_file

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
