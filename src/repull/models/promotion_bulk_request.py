from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_bulk_request_action import PromotionBulkRequestAction
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_input import PromotionInput





T = TypeVar("T", bound="PromotionBulkRequest")



@_attrs_define
class PromotionBulkRequest:
    """ 
        Attributes:
            listing_ids (list[int]):
            action (PromotionBulkRequestAction):
            promotion (PromotionInput):
     """

    listing_ids: list[int]
    action: PromotionBulkRequestAction
    promotion: PromotionInput
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_input import PromotionInput
        listing_ids = self.listing_ids



        action = self.action.value

        promotion = self.promotion.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingIds": listing_ids,
            "action": action,
            "promotion": promotion,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_input import PromotionInput
        d = dict(src_dict)
        listing_ids = cast(list[int], d.pop("listingIds"))


        action = PromotionBulkRequestAction(d.pop("action"))




        promotion = PromotionInput.from_dict(d.pop("promotion"))




        promotion_bulk_request = cls(
            listing_ids=listing_ids,
            action=action,
            promotion=promotion,
        )


        promotion_bulk_request.additional_properties = d
        return promotion_bulk_request

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
