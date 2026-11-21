from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_photo_response_200_data_items_item import UpdateVrboListingPhotoResponse200DataItemsItem
  from ..models.update_vrbo_listing_photo_response_200_data_rejected_item import UpdateVrboListingPhotoResponse200DataRejectedItem





T = TypeVar("T", bound="UpdateVrboListingPhotoResponse200Data")



@_attrs_define
class UpdateVrboListingPhotoResponse200Data:
    """ What Vrbo has after the write, read back from Vrbo.

        Attributes:
            items (list[UpdateVrboListingPhotoResponse200DataItemsItem] | Unset):
            count (int | Unset):
            rejected (list[UpdateVrboListingPhotoResponse200DataRejectedItem] | Unset):
     """

    items: list[UpdateVrboListingPhotoResponse200DataItemsItem] | Unset = UNSET
    count: int | Unset = UNSET
    rejected: list[UpdateVrboListingPhotoResponse200DataRejectedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_photo_response_200_data_items_item import UpdateVrboListingPhotoResponse200DataItemsItem
        from ..models.update_vrbo_listing_photo_response_200_data_rejected_item import UpdateVrboListingPhotoResponse200DataRejectedItem
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        count = self.count

        rejected: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rejected, Unset):
            rejected = []
            for rejected_item_data in self.rejected:
                rejected_item = rejected_item_data.to_dict()
                rejected.append(rejected_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if count is not UNSET:
            field_dict["count"] = count
        if rejected is not UNSET:
            field_dict["rejected"] = rejected

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_photo_response_200_data_items_item import UpdateVrboListingPhotoResponse200DataItemsItem
        from ..models.update_vrbo_listing_photo_response_200_data_rejected_item import UpdateVrboListingPhotoResponse200DataRejectedItem
        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[UpdateVrboListingPhotoResponse200DataItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = UpdateVrboListingPhotoResponse200DataItemsItem.from_dict(items_item_data)



                items.append(items_item)


        count = d.pop("count", UNSET)

        _rejected = d.pop("rejected", UNSET)
        rejected: list[UpdateVrboListingPhotoResponse200DataRejectedItem] | Unset = UNSET
        if _rejected is not UNSET:
            rejected = []
            for rejected_item_data in _rejected:
                rejected_item = UpdateVrboListingPhotoResponse200DataRejectedItem.from_dict(rejected_item_data)



                rejected.append(rejected_item)


        update_vrbo_listing_photo_response_200_data = cls(
            items=items,
            count=count,
            rejected=rejected,
        )


        update_vrbo_listing_photo_response_200_data.additional_properties = d
        return update_vrbo_listing_photo_response_200_data

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
