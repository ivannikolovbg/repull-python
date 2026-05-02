from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.review import Review





T = TypeVar("T", bound="ReviewGetResponse")



@_attrs_define
class ReviewGetResponse:
    """ 
        Attributes:
            data (Review | Unset): A guest or host review unified across channels. Returned by `GET /v1/reviews` and `GET
                /v1/reviews/{id}`. Populated from main vanio's unified `reviews` table after the per-channel backfill cron has
                run.
     """

    data: Review | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.review import Review
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review import Review
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Review | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = Review.from_dict(_data)




        review_get_response = cls(
            data=data,
        )


        review_get_response.additional_properties = d
        return review_get_response

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
