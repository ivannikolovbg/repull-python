from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.add_vrbo_listing_room_response_200_data_bed_types_item_sizes_item import AddVrboListingRoomResponse200DataBedTypesItemSizesItem





T = TypeVar("T", bound="AddVrboListingRoomResponse200DataBedTypesItem")



@_attrs_define
class AddVrboListingRoomResponse200DataBedTypesItem:
    """ 
        Attributes:
            value (str | Unset):
            label (None | str | Unset):
            sizes (list[AddVrboListingRoomResponse200DataBedTypesItemSizesItem] | Unset):
     """

    value: str | Unset = UNSET
    label: None | str | Unset = UNSET
    sizes: list[AddVrboListingRoomResponse200DataBedTypesItemSizesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_vrbo_listing_room_response_200_data_bed_types_item_sizes_item import AddVrboListingRoomResponse200DataBedTypesItemSizesItem
        value = self.value

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        sizes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sizes, Unset):
            sizes = []
            for sizes_item_data in self.sizes:
                sizes_item = sizes_item_data.to_dict()
                sizes.append(sizes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if value is not UNSET:
            field_dict["value"] = value
        if label is not UNSET:
            field_dict["label"] = label
        if sizes is not UNSET:
            field_dict["sizes"] = sizes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_vrbo_listing_room_response_200_data_bed_types_item_sizes_item import AddVrboListingRoomResponse200DataBedTypesItemSizesItem
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        _sizes = d.pop("sizes", UNSET)
        sizes: list[AddVrboListingRoomResponse200DataBedTypesItemSizesItem] | Unset = UNSET
        if _sizes is not UNSET:
            sizes = []
            for sizes_item_data in _sizes:
                sizes_item = AddVrboListingRoomResponse200DataBedTypesItemSizesItem.from_dict(sizes_item_data)



                sizes.append(sizes_item)


        add_vrbo_listing_room_response_200_data_bed_types_item = cls(
            value=value,
            label=label,
            sizes=sizes,
        )


        add_vrbo_listing_room_response_200_data_bed_types_item.additional_properties = d
        return add_vrbo_listing_room_response_200_data_bed_types_item

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
