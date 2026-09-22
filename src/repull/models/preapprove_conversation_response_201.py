from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.preapprove_conversation_response_201_status import PreapproveConversationResponse201Status
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PreapproveConversationResponse201")



@_attrs_define
class PreapproveConversationResponse201:
    """ 
        Attributes:
            conversation_id (str):  Example: 164743.
            status (PreapproveConversationResponse201Status):
            block_instant_booking (bool):
            expires_at (datetime.datetime | None): When the guest can no longer book on the pre-approval, if Airbnb reported
                it.
     """

    conversation_id: str
    status: PreapproveConversationResponse201Status
    block_instant_booking: bool
    expires_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        status = self.status.value

        block_instant_booking = self.block_instant_booking

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conversationId": conversation_id,
            "status": status,
            "blockInstantBooking": block_instant_booking,
            "expiresAt": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId")

        status = PreapproveConversationResponse201Status(d.pop("status"))




        block_instant_booking = d.pop("blockInstantBooking")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))


        preapprove_conversation_response_201 = cls(
            conversation_id=conversation_id,
            status=status,
            block_instant_booking=block_instant_booking,
            expires_at=expires_at,
        )


        preapprove_conversation_response_201.additional_properties = d
        return preapprove_conversation_response_201

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
