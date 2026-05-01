from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paginated_response_pagination import PaginatedResponsePagination
  from ..models.property_ import Property





T = TypeVar("T", bound="GetV1GuestsResponse200")



@_attrs_define
class GetV1GuestsResponse200:
    """ 
        Attributes:
            data (list[Property] | Unset):
            pagination (PaginatedResponsePagination | Unset):
     """

    data: list[Property] | Unset = UNSET
    pagination: PaginatedResponsePagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_response_pagination import PaginatedResponsePagination
        from ..models.property_ import Property
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
        from ..models.paginated_response_pagination import PaginatedResponsePagination
        from ..models.property_ import Property
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[Property] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Property.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: PaginatedResponsePagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = PaginatedResponsePagination.from_dict(_pagination)




        get_v1_guests_response_200 = cls(
            data=data,
            pagination=pagination,
        )


        get_v1_guests_response_200.additional_properties = d
        return get_v1_guests_response_200

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
