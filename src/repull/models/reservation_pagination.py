from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReservationPagination")



@_attrs_define
class ReservationPagination:
    """ Hybrid pagination envelope for `/v1/reservations`. Always populates `next_cursor` + `has_more` + `total`. When the
    request used the deprecated `?offset=` path, also populates `limit` + `offset`.

        Attributes:
            next_cursor (None | str): Opaque base64 cursor — pass back as `?cursor=<value>`. `null` when there are no more
                pages.
            has_more (bool):
            total (int): Total rows matching the current filter (across all pages).
            limit (int | Unset): Deprecated — only present on responses to `?offset=` requests.
            offset (int | Unset): Deprecated — only present on responses to `?offset=` requests.
     """

    next_cursor: None | str
    has_more: bool
    total: int
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        total = self.total

        limit = self.limit

        offset = self.offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_cursor": next_cursor,
            "has_more": has_more,
            "total": total,
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        has_more = d.pop("has_more")

        total = d.pop("total")

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        reservation_pagination = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            total=total,
            limit=limit,
            offset=offset,
        )


        reservation_pagination.additional_properties = d
        return reservation_pagination

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
