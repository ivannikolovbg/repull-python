from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_photo_position import AirbnbPhotoPosition





T = TypeVar("T", bound="SetAirbnbListingCoverPhotoResponse200Data")



@_attrs_define
class SetAirbnbListingCoverPhotoResponse200Data:
    """ 
        Attributes:
            cover_photo_id (str | Unset):
            applied (list[AirbnbPhotoPosition] | Unset): The photos this call actually moved. Empty when the photo was
                already the cover.
            order (list[AirbnbPhotoPosition] | Unset): Present only when the whole tour had to be renumbered.
     """

    cover_photo_id: str | Unset = UNSET
    applied: list[AirbnbPhotoPosition] | Unset = UNSET
    order: list[AirbnbPhotoPosition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_photo_position import AirbnbPhotoPosition
        cover_photo_id = self.cover_photo_id

        applied: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = []
            for applied_item_data in self.applied:
                applied_item = applied_item_data.to_dict()
                applied.append(applied_item)



        order: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = []
            for order_item_data in self.order:
                order_item = order_item_data.to_dict()
                order.append(order_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cover_photo_id is not UNSET:
            field_dict["coverPhotoId"] = cover_photo_id
        if applied is not UNSET:
            field_dict["applied"] = applied
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_photo_position import AirbnbPhotoPosition
        d = dict(src_dict)
        cover_photo_id = d.pop("coverPhotoId", UNSET)

        _applied = d.pop("applied", UNSET)
        applied: list[AirbnbPhotoPosition] | Unset = UNSET
        if _applied is not UNSET:
            applied = []
            for applied_item_data in _applied:
                applied_item = AirbnbPhotoPosition.from_dict(applied_item_data)



                applied.append(applied_item)


        _order = d.pop("order", UNSET)
        order: list[AirbnbPhotoPosition] | Unset = UNSET
        if _order is not UNSET:
            order = []
            for order_item_data in _order:
                order_item = AirbnbPhotoPosition.from_dict(order_item_data)



                order.append(order_item)


        set_airbnb_listing_cover_photo_response_200_data = cls(
            cover_photo_id=cover_photo_id,
            applied=applied,
            order=order,
        )


        set_airbnb_listing_cover_photo_response_200_data.additional_properties = d
        return set_airbnb_listing_cover_photo_response_200_data

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
