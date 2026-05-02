from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation import Reservation
  from ..models.reservation_pagination import ReservationPagination





T = TypeVar("T", bound="ReservationListResponse")



@_attrs_define
class ReservationListResponse:
    """ Cursor-paginated reservation list. Pass `pagination.next_cursor` back as `?cursor=` to fetch the next page; stop
    when `pagination.has_more` is `false`. The `total` field is the count of rows matching the current filter (across
    all pages).

    Legacy `?offset=` consumers continue to receive `pagination.limit` + `pagination.offset` during the deprecation
    window. A `Deprecation: true` header (with a `Sunset` date) is set on responses that came in via `?offset=` —
    migrate to `?cursor=`.

        Attributes:
            data (list[Reservation] | Unset):
            pagination (ReservationPagination | Unset): Hybrid pagination envelope for `/v1/reservations`. Always populates
                `next_cursor` + `has_more` + `total`. When the request used the deprecated `?offset=` path, also populates
                `limit` + `offset`.
     """

    data: list[Reservation] | Unset = UNSET
    pagination: ReservationPagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation import Reservation
        from ..models.reservation_pagination import ReservationPagination
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
        from ..models.reservation import Reservation
        from ..models.reservation_pagination import ReservationPagination
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[Reservation] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Reservation.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: ReservationPagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = ReservationPagination.from_dict(_pagination)




        reservation_list_response = cls(
            data=data,
            pagination=pagination,
        )


        reservation_list_response.additional_properties = d
        return reservation_list_response

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
