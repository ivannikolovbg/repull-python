from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Conversation")



@_attrs_define
class Conversation:
    """ 
        Attributes:
            id (str | Unset):
            reservation_id (int | Unset):
            guest_name (str | Unset):
            last_message (str | Unset):
            last_message_at (datetime.datetime | Unset):
            unread_count (int | Unset):
     """

    id: str | Unset = UNSET
    reservation_id: int | Unset = UNSET
    guest_name: str | Unset = UNSET
    last_message: str | Unset = UNSET
    last_message_at: datetime.datetime | Unset = UNSET
    unread_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reservation_id = self.reservation_id

        guest_name = self.guest_name

        last_message = self.last_message

        last_message_at: str | Unset = UNSET
        if not isinstance(self.last_message_at, Unset):
            last_message_at = self.last_message_at.isoformat()

        unread_count = self.unread_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        reservation_id = d.pop("reservationId", UNSET)

        guest_name = d.pop("guestName", UNSET)

        last_message = d.pop("lastMessage", UNSET)

        _last_message_at = d.pop("lastMessageAt", UNSET)
        last_message_at: datetime.datetime | Unset
        if isinstance(_last_message_at,  Unset):
            last_message_at = UNSET
        else:
            last_message_at = isoparse(_last_message_at)




        unread_count = d.pop("unreadCount", UNSET)

        conversation = cls(
            id=id,
            reservation_id=reservation_id,
            guest_name=guest_name,
            last_message=last_message,
            last_message_at=last_message_at,
            unread_count=unread_count,
        )


        conversation.additional_properties = d
        return conversation

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
