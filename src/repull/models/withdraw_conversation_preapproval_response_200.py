from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.withdraw_conversation_preapproval_response_200_status import WithdrawConversationPreapprovalResponse200Status
from typing import cast






T = TypeVar("T", bound="WithdrawConversationPreapprovalResponse200")



@_attrs_define
class WithdrawConversationPreapprovalResponse200:
    """ 
        Attributes:
            conversation_id (str):  Example: 166599.
            channel (None | str):  Example: vrbo.
            status (WithdrawConversationPreapprovalResponse200Status):
     """

    conversation_id: str
    channel: None | str
    status: WithdrawConversationPreapprovalResponse200Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        channel: None | str
        channel = self.channel

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conversationId": conversation_id,
            "channel": channel,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId")

        def _parse_channel(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        channel = _parse_channel(d.pop("channel"))


        status = WithdrawConversationPreapprovalResponse200Status(d.pop("status"))




        withdraw_conversation_preapproval_response_200 = cls(
            conversation_id=conversation_id,
            channel=channel,
            status=status,
        )


        withdraw_conversation_preapproval_response_200.additional_properties = d
        return withdraw_conversation_preapproval_response_200

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
