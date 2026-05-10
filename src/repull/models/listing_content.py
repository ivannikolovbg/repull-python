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
    """ Rich multilingual content slab for a listing — guest-facing copy sourced from `listings_descriptions` (the `en` row
    when surfaced via `?include=content`). Also returned as the AI-generated payload from `POST
    /v1/listings/{id}/generate-content` (where `title` and `amenities` are populated). All fields are individually
    nullable.

        Attributes:
            title (None | str | Unset): Public listing title. Populated only by `generate-content`; not stored on
                `listings_descriptions`.
            summary (None | str | Unset):
            description (None | str | Unset):
            space (None | str | Unset):
            guest_access (None | str | Unset):
            neighborhood_overview (None | str | Unset):
            getting_around (None | str | Unset): Free-text directions for getting to + around the property (e.g. "Take
                Highway 95 north for 12 miles").
            transit (None | str | Unset):
            house_rules (None | str | Unset):
            additional_rules (Any | Unset): Structured supplementary rules (JSON; shape evolves with the
                listings_descriptions schema).
            notes (None | str | Unset):
            interaction_with_guests (None | str | Unset): Host’s description of how they engage with guests (e.g. "Self
                check-in, available via message").
            amenities (list[str] | Unset): Free-text amenity strings. Populated only by `generate-content`; the
                `?include=amenities` expansion returns the structured `ListingAmenity[]` instead.
     """

    title: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    space: None | str | Unset = UNSET
    guest_access: None | str | Unset = UNSET
    neighborhood_overview: None | str | Unset = UNSET
    getting_around: None | str | Unset = UNSET
    transit: None | str | Unset = UNSET
    house_rules: None | str | Unset = UNSET
    additional_rules: Any | Unset = UNSET
    notes: None | str | Unset = UNSET
    interaction_with_guests: None | str | Unset = UNSET
    amenities: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        space: None | str | Unset
        if isinstance(self.space, Unset):
            space = UNSET
        else:
            space = self.space

        guest_access: None | str | Unset
        if isinstance(self.guest_access, Unset):
            guest_access = UNSET
        else:
            guest_access = self.guest_access

        neighborhood_overview: None | str | Unset
        if isinstance(self.neighborhood_overview, Unset):
            neighborhood_overview = UNSET
        else:
            neighborhood_overview = self.neighborhood_overview

        getting_around: None | str | Unset
        if isinstance(self.getting_around, Unset):
            getting_around = UNSET
        else:
            getting_around = self.getting_around

        transit: None | str | Unset
        if isinstance(self.transit, Unset):
            transit = UNSET
        else:
            transit = self.transit

        house_rules: None | str | Unset
        if isinstance(self.house_rules, Unset):
            house_rules = UNSET
        else:
            house_rules = self.house_rules

        additional_rules = self.additional_rules

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        interaction_with_guests: None | str | Unset
        if isinstance(self.interaction_with_guests, Unset):
            interaction_with_guests = UNSET
        else:
            interaction_with_guests = self.interaction_with_guests

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
        if getting_around is not UNSET:
            field_dict["gettingAround"] = getting_around
        if transit is not UNSET:
            field_dict["transit"] = transit
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules
        if additional_rules is not UNSET:
            field_dict["additionalRules"] = additional_rules
        if notes is not UNSET:
            field_dict["notes"] = notes
        if interaction_with_guests is not UNSET:
            field_dict["interactionWithGuests"] = interaction_with_guests
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        space = _parse_space(d.pop("space", UNSET))


        def _parse_guest_access(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_access = _parse_guest_access(d.pop("guestAccess", UNSET))


        def _parse_neighborhood_overview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        neighborhood_overview = _parse_neighborhood_overview(d.pop("neighborhoodOverview", UNSET))


        def _parse_getting_around(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        getting_around = _parse_getting_around(d.pop("gettingAround", UNSET))


        def _parse_transit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transit = _parse_transit(d.pop("transit", UNSET))


        def _parse_house_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_rules = _parse_house_rules(d.pop("houseRules", UNSET))


        additional_rules = d.pop("additionalRules", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_interaction_with_guests(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interaction_with_guests = _parse_interaction_with_guests(d.pop("interactionWithGuests", UNSET))


        amenities = cast(list[str], d.pop("amenities", UNSET))


        listing_content = cls(
            title=title,
            summary=summary,
            description=description,
            space=space,
            guest_access=guest_access,
            neighborhood_overview=neighborhood_overview,
            getting_around=getting_around,
            transit=transit,
            house_rules=house_rules,
            additional_rules=additional_rules,
            notes=notes,
            interaction_with_guests=interaction_with_guests,
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
