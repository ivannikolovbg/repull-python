from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AirbnbPhotoPosition")



@_attrs_define
class AirbnbPhotoPosition:
    """ One photo's position in the tour. `sortOrder` is a relative sort key, not an address — lower sorts earlier.

        Attributes:
            photo_id (str | Unset): Airbnb-side photo id.
            sort_order (int | Unset): Position in the tour, 1 first.
     """

    photo_id: str | Unset = UNSET
    sort_order: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        photo_id = self.photo_id

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if photo_id is not UNSET:
            field_dict["photoId"] = photo_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_id = d.pop("photoId", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        airbnb_photo_position = cls(
            photo_id=photo_id,
            sort_order=sort_order,
        )


        airbnb_photo_position.additional_properties = d
        return airbnb_photo_position

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
