from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetUsageLogsResponse200Pagination")



@_attrs_define
class GetUsageLogsResponse200Pagination:
    """ 
        Attributes:
            next_cursor (None | str | Unset):
            has_more (bool | Unset):
            total (int | Unset):
     """

    next_cursor: None | str | Unset = UNSET
    has_more: bool | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        has_more = self.has_more

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))


        has_more = d.pop("has_more", UNSET)

        total = d.pop("total", UNSET)

        get_usage_logs_response_200_pagination = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            total=total,
        )


        get_usage_logs_response_200_pagination.additional_properties = d
        return get_usage_logs_response_200_pagination

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
