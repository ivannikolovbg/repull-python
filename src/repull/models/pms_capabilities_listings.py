from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PmsCapabilitiesListings")



@_attrs_define
class PmsCapabilitiesListings:
    """ Sections `PUT /v1/listings/{id}/content` writes to the PMS.

        Attributes:
            title (bool | Unset):
            descriptions (bool | Unset):
            times (bool | Unset):
            capacity (bool | Unset):
            amenities (bool | Unset):
            house_rules (bool | Unset):
            address (bool | Unset):
            photos_add (bool | Unset):
            photos_delete (bool | Unset):
            photos_reorder (bool | Unset):
            photo_captions (bool | Unset):
     """

    title: bool | Unset = UNSET
    descriptions: bool | Unset = UNSET
    times: bool | Unset = UNSET
    capacity: bool | Unset = UNSET
    amenities: bool | Unset = UNSET
    house_rules: bool | Unset = UNSET
    address: bool | Unset = UNSET
    photos_add: bool | Unset = UNSET
    photos_delete: bool | Unset = UNSET
    photos_reorder: bool | Unset = UNSET
    photo_captions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        descriptions = self.descriptions

        times = self.times

        capacity = self.capacity

        amenities = self.amenities

        house_rules = self.house_rules

        address = self.address

        photos_add = self.photos_add

        photos_delete = self.photos_delete

        photos_reorder = self.photos_reorder

        photo_captions = self.photo_captions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if times is not UNSET:
            field_dict["times"] = times
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules
        if address is not UNSET:
            field_dict["address"] = address
        if photos_add is not UNSET:
            field_dict["photosAdd"] = photos_add
        if photos_delete is not UNSET:
            field_dict["photosDelete"] = photos_delete
        if photos_reorder is not UNSET:
            field_dict["photosReorder"] = photos_reorder
        if photo_captions is not UNSET:
            field_dict["photoCaptions"] = photo_captions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        descriptions = d.pop("descriptions", UNSET)

        times = d.pop("times", UNSET)

        capacity = d.pop("capacity", UNSET)

        amenities = d.pop("amenities", UNSET)

        house_rules = d.pop("houseRules", UNSET)

        address = d.pop("address", UNSET)

        photos_add = d.pop("photosAdd", UNSET)

        photos_delete = d.pop("photosDelete", UNSET)

        photos_reorder = d.pop("photosReorder", UNSET)

        photo_captions = d.pop("photoCaptions", UNSET)

        pms_capabilities_listings = cls(
            title=title,
            descriptions=descriptions,
            times=times,
            capacity=capacity,
            amenities=amenities,
            house_rules=house_rules,
            address=address,
            photos_add=photos_add,
            photos_delete=photos_delete,
            photos_reorder=photos_reorder,
            photo_captions=photo_captions,
        )


        pms_capabilities_listings.additional_properties = d
        return pms_capabilities_listings

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
