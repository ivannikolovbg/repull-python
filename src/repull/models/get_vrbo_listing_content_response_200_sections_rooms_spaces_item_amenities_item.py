from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsRoomsSpacesItemAmenitiesItem")



@_attrs_define
class GetVrboListingContentResponse200SectionsRoomsSpacesItemAmenitiesItem:
    """ 
        Attributes:
            id (str | Unset):
            label (None | str | Unset):
            selected (bool | Unset):
            detail_id (None | str | Unset):
            detail (None | str | Unset):
     """

    id: str | Unset = UNSET
    label: None | str | Unset = UNSET
    selected: bool | Unset = UNSET
    detail_id: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        selected = self.selected

        detail_id: None | str | Unset
        if isinstance(self.detail_id, Unset):
            detail_id = UNSET
        else:
            detail_id = self.detail_id

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if selected is not UNSET:
            field_dict["selected"] = selected
        if detail_id is not UNSET:
            field_dict["detailId"] = detail_id
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        selected = d.pop("selected", UNSET)

        def _parse_detail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail_id = _parse_detail_id(d.pop("detailId", UNSET))


        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        get_vrbo_listing_content_response_200_sections_rooms_spaces_item_amenities_item = cls(
            id=id,
            label=label,
            selected=selected,
            detail_id=detail_id,
            detail=detail,
        )


        get_vrbo_listing_content_response_200_sections_rooms_spaces_item_amenities_item.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_rooms_spaces_item_amenities_item

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
