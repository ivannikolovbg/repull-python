from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DeleteVrboListingRoomResponse200DataSpacesItemBedsItem")



@_attrs_define
class DeleteVrboListingRoomResponse200DataSpacesItemBedsItem:
    """ 
        Attributes:
            type_ (str | Unset):  Example: QUEEN_BED.
            size (None | str | Unset):  Example: QUEEN.
            quantity (int | Unset):
     """

    type_: str | Unset = UNSET
    size: None | str | Unset = UNSET
    quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        size: None | str | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if size is not UNSET:
            field_dict["size"] = size
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        size = _parse_size(d.pop("size", UNSET))


        quantity = d.pop("quantity", UNSET)

        delete_vrbo_listing_room_response_200_data_spaces_item_beds_item = cls(
            type_=type_,
            size=size,
            quantity=quantity,
        )


        delete_vrbo_listing_room_response_200_data_spaces_item_beds_item.additional_properties = d
        return delete_vrbo_listing_room_response_200_data_spaces_item_beds_item

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
