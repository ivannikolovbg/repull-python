from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WebhookSubscription")



@_attrs_define
class WebhookSubscription:
    """ 
        Attributes:
            id (str | Unset):
            url (str | Unset):
            events (list[str] | Unset):  Example: ['reservation.created', 'reservation.updated'].
            active (bool | Unset):
            secret (str | Unset): HMAC-SHA256 signing secret
     """

    id: str | Unset = UNSET
    url: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    active: bool | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events



        active = self.active

        secret = self.secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        events = cast(list[str], d.pop("events", UNSET))


        active = d.pop("active", UNSET)

        secret = d.pop("secret", UNSET)

        webhook_subscription = cls(
            id=id,
            url=url,
            events=events,
            active=active,
            secret=secret,
        )


        webhook_subscription.additional_properties = d
        return webhook_subscription

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
