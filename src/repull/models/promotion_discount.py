from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_discount_set_by import PromotionDiscountSetBy
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PromotionDiscount")



@_attrs_define
class PromotionDiscount:
    """ 
        Attributes:
            percent (float | None | Unset):
            set_by (PromotionDiscountSetBy | Unset):
     """

    percent: float | None | Unset = UNSET
    set_by: PromotionDiscountSetBy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        percent: float | None | Unset
        if isinstance(self.percent, Unset):
            percent = UNSET
        else:
            percent = self.percent

        set_by: str | Unset = UNSET
        if not isinstance(self.set_by, Unset):
            set_by = self.set_by.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if percent is not UNSET:
            field_dict["percent"] = percent
        if set_by is not UNSET:
            field_dict["setBy"] = set_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent = _parse_percent(d.pop("percent", UNSET))


        _set_by = d.pop("setBy", UNSET)
        set_by: PromotionDiscountSetBy | Unset
        if isinstance(_set_by,  Unset):
            set_by = UNSET
        else:
            set_by = PromotionDiscountSetBy(_set_by)




        promotion_discount = cls(
            percent=percent,
            set_by=set_by,
        )


        promotion_discount.additional_properties = d
        return promotion_discount

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
