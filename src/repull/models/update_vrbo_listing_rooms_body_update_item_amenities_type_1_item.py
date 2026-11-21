from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item")



@_attrs_define
class UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item:
    """ 
        Attributes:
            id (str | Unset):
            selected (bool | Unset):
            detail (str | Unset):
     """

    id: str | Unset = UNSET
    selected: bool | Unset = UNSET
    detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        selected = self.selected

        detail = self.detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if selected is not UNSET:
            field_dict["selected"] = selected
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        selected = d.pop("selected", UNSET)

        detail = d.pop("detail", UNSET)

        update_vrbo_listing_rooms_body_update_item_amenities_type_1_item = cls(
            id=id,
            selected=selected,
            detail=detail,
        )


        update_vrbo_listing_rooms_body_update_item_amenities_type_1_item.additional_properties = d
        return update_vrbo_listing_rooms_body_update_item_amenities_type_1_item

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
