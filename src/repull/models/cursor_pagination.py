from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CursorPagination")



@_attrs_define
class CursorPagination:
    """ Canonical cursor-based pagination envelope. Pass `nextCursor` back as `?cursor=` to fetch the next page; stop when
    `hasMore` is `false`. The cursor is opaque base64 — do not parse or construct it by hand.

        Attributes:
            next_cursor (None | str): Opaque base64 cursor — pass back as `?cursor=<value>`. `null` when there are no more
                pages.
            has_more (bool):
            total (int | Unset): Total rows matching the current filter (across all pages). Present when
                `?include_total=true` (the default on most endpoints). Omit `?include_total=false` to skip the COUNT(*) on very
                large workspaces.
     """

    next_cursor: None | str
    has_more: bool
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nextCursor": next_cursor,
            "hasMore": has_more,
        })
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))


        has_more = d.pop("hasMore")

        total = d.pop("total", UNSET)

        cursor_pagination = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            total=total,
        )


        cursor_pagination.additional_properties = d
        return cursor_pagination

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
