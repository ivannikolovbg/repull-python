from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbDescriptionWriteRequestDescription")



@_attrs_define
class AirbnbDescriptionWriteRequestDescription:
    """ At least one field required. `description` itself is NOT accepted: Airbnb composes the public description from these
    sections and ignores a directly-supplied one, so accepting it would be taking a value and discarding it. An unknown
    field is refused by name rather than dropped.

        Attributes:
            name (None | str | Unset):
            summary (None | str | Unset): Airbnb hard-caps this at 500 characters and refuses the whole write if it is
                longer.
            space (None | str | Unset):
            access (None | str | Unset):
            interaction (None | str | Unset):
            neighborhood_overview (None | str | Unset):
            transit (None | str | Unset):
            notes (None | str | Unset):
            house_rules (None | str | Unset):
     """

    name: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    space: None | str | Unset = UNSET
    access: None | str | Unset = UNSET
    interaction: None | str | Unset = UNSET
    neighborhood_overview: None | str | Unset = UNSET
    transit: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    house_rules: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        space: None | str | Unset
        if isinstance(self.space, Unset):
            space = UNSET
        else:
            space = self.space

        access: None | str | Unset
        if isinstance(self.access, Unset):
            access = UNSET
        else:
            access = self.access

        interaction: None | str | Unset
        if isinstance(self.interaction, Unset):
            interaction = UNSET
        else:
            interaction = self.interaction

        neighborhood_overview: None | str | Unset
        if isinstance(self.neighborhood_overview, Unset):
            neighborhood_overview = UNSET
        else:
            neighborhood_overview = self.neighborhood_overview

        transit: None | str | Unset
        if isinstance(self.transit, Unset):
            transit = UNSET
        else:
            transit = self.transit

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        house_rules: None | str | Unset
        if isinstance(self.house_rules, Unset):
            house_rules = UNSET
        else:
            house_rules = self.house_rules


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if space is not UNSET:
            field_dict["space"] = space
        if access is not UNSET:
            field_dict["access"] = access
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        if neighborhood_overview is not UNSET:
            field_dict["neighborhood_overview"] = neighborhood_overview
        if transit is not UNSET:
            field_dict["transit"] = transit
        if notes is not UNSET:
            field_dict["notes"] = notes
        if house_rules is not UNSET:
            field_dict["house_rules"] = house_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_space(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        space = _parse_space(d.pop("space", UNSET))


        def _parse_access(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access = _parse_access(d.pop("access", UNSET))


        def _parse_interaction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interaction = _parse_interaction(d.pop("interaction", UNSET))


        def _parse_neighborhood_overview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        neighborhood_overview = _parse_neighborhood_overview(d.pop("neighborhood_overview", UNSET))


        def _parse_transit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transit = _parse_transit(d.pop("transit", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_house_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_rules = _parse_house_rules(d.pop("house_rules", UNSET))


        airbnb_description_write_request_description = cls(
            name=name,
            summary=summary,
            space=space,
            access=access,
            interaction=interaction,
            neighborhood_overview=neighborhood_overview,
            transit=transit,
            notes=notes,
            house_rules=house_rules,
        )

        return airbnb_description_write_request_description

