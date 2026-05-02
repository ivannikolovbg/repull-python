from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContent")



@_attrs_define
class ListingContent:
    """ 
        Attributes:
            title (str | Unset):
            summary (str | Unset):
            description (str | Unset):
            space (str | Unset):
            guest_access (str | Unset):
            neighborhood_overview (str | Unset):
            transit (str | Unset):
            notes (str | Unset):
            house_rules (str | Unset):
            amenities (list[str] | Unset):
     """

    title: str | Unset = UNSET
    summary: str | Unset = UNSET
    description: str | Unset = UNSET
    space: str | Unset = UNSET
    guest_access: str | Unset = UNSET
    neighborhood_overview: str | Unset = UNSET
    transit: str | Unset = UNSET
    notes: str | Unset = UNSET
    house_rules: str | Unset = UNSET
    amenities: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        summary = self.summary

        description = self.description

        space = self.space

        guest_access = self.guest_access

        neighborhood_overview = self.neighborhood_overview

        transit = self.transit

        notes = self.notes

        house_rules = self.house_rules

        amenities: list[str] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = self.amenities




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if space is not UNSET:
            field_dict["space"] = space
        if guest_access is not UNSET:
            field_dict["guestAccess"] = guest_access
        if neighborhood_overview is not UNSET:
            field_dict["neighborhoodOverview"] = neighborhood_overview
        if transit is not UNSET:
            field_dict["transit"] = transit
        if notes is not UNSET:
            field_dict["notes"] = notes
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        space = d.pop("space", UNSET)

        guest_access = d.pop("guestAccess", UNSET)

        neighborhood_overview = d.pop("neighborhoodOverview", UNSET)

        transit = d.pop("transit", UNSET)

        notes = d.pop("notes", UNSET)

        house_rules = d.pop("houseRules", UNSET)

        amenities = cast(list[str], d.pop("amenities", UNSET))


        listing_content = cls(
            title=title,
            summary=summary,
            description=description,
            space=space,
            guest_access=guest_access,
            neighborhood_overview=neighborhood_overview,
            transit=transit,
            notes=notes,
            house_rules=house_rules,
            amenities=amenities,
        )


        listing_content.additional_properties = d
        return listing_content

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
