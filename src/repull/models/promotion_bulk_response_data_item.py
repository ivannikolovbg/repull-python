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
  from ..models.promotion_bulk_response_data_item_error import PromotionBulkResponseDataItemError





T = TypeVar("T", bound="PromotionBulkResponseDataItem")



@_attrs_define
class PromotionBulkResponseDataItem:
    """ 
        Attributes:
            listing_id (str | Unset):
            ok (bool | Unset):
            promotion (Promotion | Unset): One promotion on one listing. Airbnb sets the discount for its promotions
                (`discount.setBy: channel`); Booking.com promotions belong to the property and list the rooms they cover in
                `appliesTo`.
            error (PromotionBulkResponseDataItemError | Unset):
     """

    listing_id: str | Unset = UNSET
    ok: bool | Unset = UNSET
    promotion: Promotion | Unset = UNSET
    error: PromotionBulkResponseDataItemError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion import Promotion
        from ..models.promotion_bulk_response_data_item_error import PromotionBulkResponseDataItemError
        listing_id = self.listing_id

        ok = self.ok

        promotion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.promotion, Unset):
            promotion = self.promotion.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if ok is not UNSET:
            field_dict["ok"] = ok
        if promotion is not UNSET:
            field_dict["promotion"] = promotion
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion import Promotion
        from ..models.promotion_bulk_response_data_item_error import PromotionBulkResponseDataItemError
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        ok = d.pop("ok", UNSET)

        _promotion = d.pop("promotion", UNSET)
        promotion: Promotion | Unset
        if isinstance(_promotion,  Unset):
            promotion = UNSET
        else:
            promotion = Promotion.from_dict(_promotion)




        _error = d.pop("error", UNSET)
        error: PromotionBulkResponseDataItemError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = PromotionBulkResponseDataItemError.from_dict(_error)




        promotion_bulk_response_data_item = cls(
            listing_id=listing_id,
            ok=ok,
            promotion=promotion,
            error=error,
        )


        promotion_bulk_response_data_item.additional_properties = d
        return promotion_bulk_response_data_item

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
