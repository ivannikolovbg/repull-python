from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversation_platform import ConversationPlatform
from ..models.conversation_status import ConversationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Conversation")



@_attrs_define
class Conversation:
    """ Channel-agnostic message thread between the host workspace and a guest. Returned by `GET /v1/conversations`. The
    `id` is the internal Repull thread id (integer) — pass it back as the `{id}` path param on detail / messages calls.

        Attributes:
            id (str | Unset):
            platform (ConversationPlatform | Unset):  Example: airbnb.
            guest_id (None | str | Unset):
            listing_id (None | str | Unset):
            reservation_id (None | str | Unset):
            subject (None | str | Unset): Thread subject (email/website channels) or null when not applicable.
            last_message_at (datetime.datetime | None | Unset):
            last_message_preview (None | str | Unset): Short preview of the most recent message body for list-UI rendering.
            unread_count (int | Unset):
            status (ConversationStatus | Unset): `archived` is reserved for a future bit on `message_threads` — currently
                always `open`.
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    platform: ConversationPlatform | Unset = UNSET
    guest_id: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    reservation_id: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    last_message_preview: None | str | Unset = UNSET
    unread_count: int | Unset = UNSET
    status: ConversationStatus | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value


        guest_id: None | str | Unset
        if isinstance(self.guest_id, Unset):
            guest_id = UNSET
        else:
            guest_id = self.guest_id

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        last_message_preview: None | str | Unset
        if isinstance(self.last_message_preview, Unset):
            last_message_preview = UNSET
        else:
            last_message_preview = self.last_message_preview

        unread_count = self.unread_count

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if last_message_preview is not UNSET:
            field_dict["lastMessagePreview"] = last_message_preview
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ConversationPlatform | Unset
        if isinstance(_platform,  Unset):
            platform = UNSET
        else:
            platform = ConversationPlatform(_platform)




        def _parse_guest_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_id = _parse_guest_id(d.pop("guestId", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))


        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = isoparse(data)



                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("lastMessageAt", UNSET))


        def _parse_last_message_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_message_preview = _parse_last_message_preview(d.pop("lastMessagePreview", UNSET))


        unread_count = d.pop("unreadCount", UNSET)

        _status = d.pop("status", UNSET)
        status: ConversationStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConversationStatus(_status)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        conversation = cls(
            id=id,
            platform=platform,
            guest_id=guest_id,
            listing_id=listing_id,
            reservation_id=reservation_id,
            subject=subject,
            last_message_at=last_message_at,
            last_message_preview=last_message_preview,
            unread_count=unread_count,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
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
