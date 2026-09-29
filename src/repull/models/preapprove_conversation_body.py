from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PreapproveConversationBody")



@_attrs_define
class PreapproveConversationBody:
    """ 
        Attributes:
            block_instant_booking (bool | Unset): Airbnb: when `true`, the guest cannot Instant Book the listing and must
                book through this pre-approval. Leave `false` unless you need that. Default: False.
            message (str | Unset): VRBO: the message sent to the guest with the pre-approval (a friendly default otherwise).
     """

    block_instant_booking: bool | Unset = False
    message: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        block_instant_booking = self.block_instant_booking

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if block_instant_booking is not UNSET:
            field_dict["blockInstantBooking"] = block_instant_booking
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_instant_booking = d.pop("blockInstantBooking", UNSET)

        message = d.pop("message", UNSET)

        preapprove_conversation_body = cls(
            block_instant_booking=block_instant_booking,
            message=message,
        )

        return preapprove_conversation_body

