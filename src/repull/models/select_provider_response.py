from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.select_provider_response_pattern import SelectProviderResponsePattern
from ..types import UNSET, Unset






T = TypeVar("T", bound="SelectProviderResponse")



@_attrs_define
class SelectProviderResponse:
    """ Returned by `POST /v1/connect/sessions/{sessionId}/select-provider`. The picker UI navigates the user to `nextUrl`
    to begin the per-provider handoff.

        Attributes:
            session_id (str | Unset):
            provider (str | Unset):  Example: airbnb.
            pattern (SelectProviderResponsePattern | Unset):
            next_url (str | Unset): Where to send the user next — OAuth consent, credentials form, activation checklist, or
                claim form.
     """

    session_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    pattern: SelectProviderResponsePattern | Unset = UNSET
    next_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        provider = self.provider

        pattern: str | Unset = UNSET
        if not isinstance(self.pattern, Unset):
            pattern = self.pattern.value


        next_url = self.next_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if next_url is not UNSET:
            field_dict["nextUrl"] = next_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId", UNSET)

        provider = d.pop("provider", UNSET)

        _pattern = d.pop("pattern", UNSET)
        pattern: SelectProviderResponsePattern | Unset
        if isinstance(_pattern,  Unset):
            pattern = UNSET
        else:
            pattern = SelectProviderResponsePattern(_pattern)




        next_url = d.pop("nextUrl", UNSET)

        select_provider_response = cls(
            session_id=session_id,
            provider=provider,
            pattern=pattern,
            next_url=next_url,
        )


        select_provider_response.additional_properties = d
        return select_provider_response

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
