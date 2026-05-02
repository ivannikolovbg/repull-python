from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TestWebhookBody")



@_attrs_define
class TestWebhookBody:
    """ 
        Attributes:
            url (str | Unset):
            event_type (str | Unset):
            signing_secret (str | Unset):
     """

    url: str | Unset = UNSET
    event_type: str | Unset = UNSET
    signing_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        event_type = self.event_type

        signing_secret = self.signing_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if signing_secret is not UNSET:
            field_dict["signing_secret"] = signing_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        event_type = d.pop("event_type", UNSET)

        signing_secret = d.pop("signing_secret", UNSET)

        test_webhook_body = cls(
            url=url,
            event_type=event_type,
            signing_secret=signing_secret,
        )


        test_webhook_body.additional_properties = d
        return test_webhook_body

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
