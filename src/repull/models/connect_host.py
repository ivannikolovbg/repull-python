from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConnectHost")



@_attrs_define
class ConnectHost:
    """ Public-facing metadata about the host whose account is linked. Lets clients render an account-level card (avatar +
    name) instead of just an opaque ID. Email is intentionally NOT exposed for Airbnb — the partner API doesn't return
    host email.

        Attributes:
            display_name (None | str | Unset): Short display name (Airbnb first name). Example: Lidia.
            display_name_long (None | str | Unset): Preferred long-form name. Falls back to displayName when the host hasn't
                set a preferred form. Example: Lidia.
            avatar_url (None | str | Unset): Profile picture URL (small).
            avatar_url_large (None | str | Unset): Profile picture URL (large).
            activation_status (None | str | Unset): Per-provider activation/onboarding status. Example: active.
     """

    display_name: None | str | Unset = UNSET
    display_name_long: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    avatar_url_large: None | str | Unset = UNSET
    activation_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        display_name_long: None | str | Unset
        if isinstance(self.display_name_long, Unset):
            display_name_long = UNSET
        else:
            display_name_long = self.display_name_long

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        avatar_url_large: None | str | Unset
        if isinstance(self.avatar_url_large, Unset):
            avatar_url_large = UNSET
        else:
            avatar_url_large = self.avatar_url_large

        activation_status: None | str | Unset
        if isinstance(self.activation_status, Unset):
            activation_status = UNSET
        else:
            activation_status = self.activation_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_name_long is not UNSET:
            field_dict["displayNameLong"] = display_name_long
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if avatar_url_large is not UNSET:
            field_dict["avatarUrlLarge"] = avatar_url_large
        if activation_status is not UNSET:
            field_dict["activationStatus"] = activation_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        def _parse_display_name_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name_long = _parse_display_name_long(d.pop("displayNameLong", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_avatar_url_large(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url_large = _parse_avatar_url_large(d.pop("avatarUrlLarge", UNSET))


        def _parse_activation_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_status = _parse_activation_status(d.pop("activationStatus", UNSET))


        connect_host = cls(
            display_name=display_name,
            display_name_long=display_name_long,
            avatar_url=avatar_url,
            avatar_url_large=avatar_url_large,
            activation_status=activation_status,
        )


        connect_host.additional_properties = d
        return connect_host

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
