from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cursor_pagination import CursorPagination
  from ..models.review import Review





T = TypeVar("T", bound="ReviewListResponse")



@_attrs_define
class ReviewListResponse:
    """ Cursor-paginated review list. Pass `pagination.nextCursor` back as `?cursor=` to fetch the next page.

        Attributes:
            data (list[Review] | Unset):
            pagination (CursorPagination | Unset): Canonical cursor-based pagination envelope. Pass `nextCursor` back as
                `?cursor=` to fetch the next page; stop when `hasMore` is `false`. The cursor is opaque base64 — do not parse or
                construct it by hand.
     """

    data: list[Review] | Unset = UNSET
    pagination: CursorPagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cursor_pagination import CursorPagination
        from ..models.review import Review
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.review import Review
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[Review] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Review.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: CursorPagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = CursorPagination.from_dict(_pagination)




        review_list_response = cls(
            data=data,
            pagination=pagination,
        )


        review_list_response.additional_properties = d
        return review_list_response

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
