from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_bulk_response_data_item import PromotionBulkResponseDataItem
  from ..models.promotion_bulk_response_summary import PromotionBulkResponseSummary





T = TypeVar("T", bound="PromotionBulkResponse")



@_attrs_define
class PromotionBulkResponse:
    """ 
        Attributes:
            data (list[PromotionBulkResponseDataItem] | Unset):
            summary (PromotionBulkResponseSummary | Unset):
     """

    data: list[PromotionBulkResponseDataItem] | Unset = UNSET
    summary: PromotionBulkResponseSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_bulk_response_data_item import PromotionBulkResponseDataItem
        from ..models.promotion_bulk_response_summary import PromotionBulkResponseSummary
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_bulk_response_data_item import PromotionBulkResponseDataItem
        from ..models.promotion_bulk_response_summary import PromotionBulkResponseSummary
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[PromotionBulkResponseDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = PromotionBulkResponseDataItem.from_dict(data_item_data)



                data.append(data_item)


        _summary = d.pop("summary", UNSET)
        summary: PromotionBulkResponseSummary | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = PromotionBulkResponseSummary.from_dict(_summary)




        promotion_bulk_response = cls(
            data=data,
            summary=summary,
        )


        promotion_bulk_response.additional_properties = d
        return promotion_bulk_response

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
