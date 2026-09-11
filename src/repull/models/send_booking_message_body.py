from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SendBookingMessageBody")



@_attrs_define
class SendBookingMessageBody:
    """ 
        Attributes:
            property_id (int): Booking.com property (hotel) id the conversation belongs to.
            conversation_id (str): Booking.com conversation id to reply in.
            message (str): Message body to send to the guest.
     """

    property_id: int
    conversation_id: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id

        conversation_id = self.conversation_id

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "property_id": property_id,
            "conversation_id": conversation_id,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_id = d.pop("property_id")

        conversation_id = d.pop("conversation_id")

        message = d.pop("message")

        send_booking_message_body = cls(
            property_id=property_id,
            conversation_id=conversation_id,
            message=message,
        )


        send_booking_message_body.additional_properties = d
        return send_booking_message_body

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
