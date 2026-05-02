from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateWebhookBody")



@_attrs_define
class CreateWebhookBody:
    """ 
        Attributes:
            url (str):
            events (list[str]):
            description (None | str | Unset):
            api_version (str | Unset):  Example: 2026-04.
     """

    url: str
    events: list[str]
    description: None | str | Unset = UNSET
    api_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = self.events



        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        api_version = self.api_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
            "events": events,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = cast(list[str], d.pop("events"))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        api_version = d.pop("apiVersion", UNSET)

        create_webhook_body = cls(
            url=url,
            events=events,
            description=description,
            api_version=api_version,
        )


        create_webhook_body.additional_properties = d
        return create_webhook_body

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
