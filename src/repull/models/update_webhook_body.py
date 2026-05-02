from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_webhook_body_status import UpdateWebhookBodyStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateWebhookBody")



@_attrs_define
class UpdateWebhookBody:
    """ 
        Attributes:
            url (str | Unset):
            description (None | str | Unset):
            events (list[str] | Unset):
            status (UpdateWebhookBodyStatus | Unset):
     """

    url: str | Unset = UNSET
    description: None | str | Unset = UNSET
    events: list[str] | Unset = UNSET
    status: UpdateWebhookBodyStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events



        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        events = cast(list[str], d.pop("events", UNSET))


        _status = d.pop("status", UNSET)
        status: UpdateWebhookBodyStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = UpdateWebhookBodyStatus(_status)




        update_webhook_body = cls(
            url=url,
            description=description,
            events=events,
            status=status,
        )


        update_webhook_body.additional_properties = d
        return update_webhook_body

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
