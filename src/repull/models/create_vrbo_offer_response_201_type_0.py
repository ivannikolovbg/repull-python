from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateVrboOfferResponse201Type0")



@_attrs_define
class CreateVrboOfferResponse201Type0:
    """ 
        Attributes:
            conversation_id (str | Unset):
            channel (str | Unset):
            status (str | Unset):  Example: pre_approved.
            message (None | str | Unset):
     """

    conversation_id: str | Unset = UNSET
    channel: str | Unset = UNSET
    status: str | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        channel = self.channel

        status = self.status

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId", UNSET)

        channel = d.pop("channel", UNSET)

        status = d.pop("status", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        create_vrbo_offer_response_201_type_0 = cls(
            conversation_id=conversation_id,
            channel=channel,
            status=status,
            message=message,
        )


        create_vrbo_offer_response_201_type_0.additional_properties = d
        return create_vrbo_offer_response_201_type_0

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
