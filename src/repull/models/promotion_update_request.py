from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_rules import PromotionRules





T = TypeVar("T", bound="PromotionUpdateRequest")



@_attrs_define
class PromotionUpdateRequest:
    """ 
        Attributes:
            name (str | Unset):
            discount_percent (int | Unset):
            rules (PromotionRules | Unset): Which rules a type supports depends on the channel — see the catalog.
            confirm_shared (bool | Unset): Required when the promotion also covers other listings’ rooms — the change
                applies to them too.
     """

    name: str | Unset = UNSET
    discount_percent: int | Unset = UNSET
    rules: PromotionRules | Unset = UNSET
    confirm_shared: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_rules import PromotionRules
        name = self.name

        discount_percent = self.discount_percent

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        confirm_shared = self.confirm_shared


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if rules is not UNSET:
            field_dict["rules"] = rules
        if confirm_shared is not UNSET:
            field_dict["confirmShared"] = confirm_shared

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_rules import PromotionRules
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        discount_percent = d.pop("discountPercent", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: PromotionRules | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = PromotionRules.from_dict(_rules)




        confirm_shared = d.pop("confirmShared", UNSET)

        promotion_update_request = cls(
            name=name,
            discount_percent=discount_percent,
            rules=rules,
            confirm_shared=confirm_shared,
        )


        promotion_update_request.additional_properties = d
        return promotion_update_request

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
