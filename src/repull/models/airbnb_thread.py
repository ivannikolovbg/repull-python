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






T = TypeVar("T", bound="AirbnbThread")



@_attrs_define
class AirbnbThread:
    """ An Airbnb message thread.

        Attributes:
            id (str | Unset):
            listing_id (None | str | Unset):
            guest_name (None | str | Unset):
            last_message_at (datetime.datetime | None | Unset):
            unread_count (int | None | Unset):
     """

    id: str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    unread_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        unread_count: int | None | Unset
        if isinstance(self.unread_count, Unset):
            unread_count = UNSET
        else:
            unread_count = self.unread_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


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


        def _parse_unread_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unread_count = _parse_unread_count(d.pop("unreadCount", UNSET))


        airbnb_thread = cls(
            id=id,
            listing_id=listing_id,
            guest_name=guest_name,
            last_message_at=last_message_at,
            unread_count=unread_count,
        )


        airbnb_thread.additional_properties = d
        return airbnb_thread

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
