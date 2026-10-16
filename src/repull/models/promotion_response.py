from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion import Promotion





T = TypeVar("T", bound="PromotionResponse")



@_attrs_define
class PromotionResponse:
    """ 
        Attributes:
            data (Promotion | Unset): One promotion on one listing. Airbnb sets the discount for its promotions
                (`discount.setBy: channel`); Booking.com promotions belong to the property and list the rooms they cover in
                `appliesTo`.
     """

    data: Promotion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion import Promotion
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
        from ..models.promotion import Promotion
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Promotion | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = Promotion.from_dict(_data)




        promotion_response = cls(
            data=data,
        )


        promotion_response.additional_properties = d
        return promotion_response

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
