from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.withdraw_conversation_special_offer_response_200_status import WithdrawConversationSpecialOfferResponse200Status






T = TypeVar("T", bound="WithdrawConversationSpecialOfferResponse200")



@_attrs_define
class WithdrawConversationSpecialOfferResponse200:
    """ 
        Attributes:
            id (str):  Example: 1459920384.
            conversation_id (str):  Example: 164743.
            status (WithdrawConversationSpecialOfferResponse200Status):
     """

    id: str
    conversation_id: str
    status: WithdrawConversationSpecialOfferResponse200Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conversation_id = self.conversation_id

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "conversationId": conversation_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        conversation_id = d.pop("conversationId")

        status = WithdrawConversationSpecialOfferResponse200Status(d.pop("status"))




        withdraw_conversation_special_offer_response_200 = cls(
            id=id,
            conversation_id=conversation_id,
            status=status,
        )


        withdraw_conversation_special_offer_response_200.additional_properties = d
        return withdraw_conversation_special_offer_response_200

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
