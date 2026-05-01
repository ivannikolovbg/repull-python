from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostV1WebhooksTestBody")



@_attrs_define
class PostV1WebhooksTestBody:
    """ 
        Attributes:
            webhook_id (str | Unset):
            event (str | Unset):
     """

    webhook_id: str | Unset = UNSET
    event: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        webhook_id = self.webhook_id

        event = self.event


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_id = d.pop("webhookId", UNSET)

        event = d.pop("event", UNSET)

        post_v1_webhooks_test_body = cls(
            webhook_id=webhook_id,
            event=event,
        )


        post_v1_webhooks_test_body.additional_properties = d
        return post_v1_webhooks_test_body

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
