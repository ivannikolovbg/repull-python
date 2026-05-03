from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConversationHost")



@_attrs_define
class ConversationHost:
    """ Linked host metadata for a conversation thread. Currently populated for Airbnb threads (resolved through
    `airbnb_hosts`); null for other channels until per-channel host enrichment lands.

        Attributes:
            id (str | Unset):
            airbnb_id (str | Unset): Airbnb-side host id.
            first_name (str | Unset):
            display_name (str | Unset):
            avatar_url (None | str | Unset):
     """

    id: str | Unset = UNSET
    airbnb_id: str | Unset = UNSET
    first_name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        airbnb_id = self.airbnb_id

        first_name = self.first_name

        display_name = self.display_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if airbnb_id is not UNSET:
            field_dict["airbnbId"] = airbnb_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        airbnb_id = d.pop("airbnbId", UNSET)

        first_name = d.pop("firstName", UNSET)

        display_name = d.pop("displayName", UNSET)

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        conversation_host = cls(
            id=id,
            airbnb_id=airbnb_id,
            first_name=first_name,
            display_name=display_name,
            avatar_url=avatar_url,
        )


        conversation_host.additional_properties = d
        return conversation_host

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
