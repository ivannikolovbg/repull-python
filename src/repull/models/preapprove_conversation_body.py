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
            block_instant_booking (bool | Unset): When `true`, the guest cannot Instant Book the listing and must book
                through this pre-approval. Leave `false` unless you need that. Default: False.
     """

    block_instant_booking: bool | Unset = False





    def to_dict(self) -> dict[str, Any]:
        block_instant_booking = self.block_instant_booking


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if block_instant_booking is not UNSET:
            field_dict["blockInstantBooking"] = block_instant_booking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_instant_booking = d.pop("blockInstantBooking", UNSET)

        preapprove_conversation_body = cls(
            block_instant_booking=block_instant_booking,
        )

        return preapprove_conversation_body

