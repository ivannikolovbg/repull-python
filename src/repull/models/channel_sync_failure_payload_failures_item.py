from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_sync_failure_payload_failures_item_kind import ChannelSyncFailurePayloadFailuresItemKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ChannelSyncFailurePayloadFailuresItem")



@_attrs_define
class ChannelSyncFailurePayloadFailuresItem:
    """ 
        Attributes:
            channel (str | Unset):  Example: airbnb.
            external_listing_id (None | str | Unset): The channel's own id for the room or listing.
            kind (ChannelSyncFailurePayloadFailuresItemKind | Unset): `unknown` means we could not classify it — never that
                the channel refused.
            message (None | str | Unset): The channel's own message, verbatim.
     """

    channel: str | Unset = UNSET
    external_listing_id: None | str | Unset = UNSET
    kind: ChannelSyncFailurePayloadFailuresItemKind | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        external_listing_id: None | str | Unset
        if isinstance(self.external_listing_id, Unset):
            external_listing_id = UNSET
        else:
            external_listing_id = self.external_listing_id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if external_listing_id is not UNSET:
            field_dict["externalListingId"] = external_listing_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        def _parse_external_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_listing_id = _parse_external_listing_id(d.pop("externalListingId", UNSET))


        _kind = d.pop("kind", UNSET)
        kind: ChannelSyncFailurePayloadFailuresItemKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = ChannelSyncFailurePayloadFailuresItemKind(_kind)




        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        channel_sync_failure_payload_failures_item = cls(
            channel=channel,
            external_listing_id=external_listing_id,
            kind=kind,
            message=message,
        )


        channel_sync_failure_payload_failures_item.additional_properties = d
        return channel_sync_failure_payload_failures_item

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
