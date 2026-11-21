from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsHouseRulesEvents")



@_attrs_define
class GetVrboListingContentResponse200SectionsHouseRulesEvents:
    """ 
        Attributes:
            allowed (bool | None | Unset):
            max_attendees (int | None | Unset):
            allowed_events_note (None | str | Unset):
            note (None | str | Unset):
     """

    allowed: bool | None | Unset = UNSET
    max_attendees: int | None | Unset = UNSET
    allowed_events_note: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed: bool | None | Unset
        if isinstance(self.allowed, Unset):
            allowed = UNSET
        else:
            allowed = self.allowed

        max_attendees: int | None | Unset
        if isinstance(self.max_attendees, Unset):
            max_attendees = UNSET
        else:
            max_attendees = self.max_attendees

        allowed_events_note: None | str | Unset
        if isinstance(self.allowed_events_note, Unset):
            allowed_events_note = UNSET
        else:
            allowed_events_note = self.allowed_events_note

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if max_attendees is not UNSET:
            field_dict["maxAttendees"] = max_attendees
        if allowed_events_note is not UNSET:
            field_dict["allowedEventsNote"] = allowed_events_note
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allowed = _parse_allowed(d.pop("allowed", UNSET))


        def _parse_max_attendees(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_attendees = _parse_max_attendees(d.pop("maxAttendees", UNSET))


        def _parse_allowed_events_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        allowed_events_note = _parse_allowed_events_note(d.pop("allowedEventsNote", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        get_vrbo_listing_content_response_200_sections_house_rules_events = cls(
            allowed=allowed,
            max_attendees=max_attendees,
            allowed_events_note=allowed_events_note,
            note=note,
        )


        get_vrbo_listing_content_response_200_sections_house_rules_events.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_house_rules_events

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
