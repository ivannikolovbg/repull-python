from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateConnectSessionBody")



@_attrs_define
class CreateConnectSessionBody:
    """ 
        Attributes:
            redirect_url (str): Where to send the user after they finish (or cancel). Status query params are appended.
            state (None | str | Unset): Opaque pass-through correlation token. Echoed back in the response.
            allowed_providers (list[str] | None | Unset): Optional whitelist of provider IDs the picker should expose. Omit
                to show every channel in the registry.
     """

    redirect_url: str
    state: None | str | Unset = UNSET
    allowed_providers: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        redirect_url = self.redirect_url

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        allowed_providers: list[str] | None | Unset
        if isinstance(self.allowed_providers, Unset):
            allowed_providers = UNSET
        elif isinstance(self.allowed_providers, list):
            allowed_providers = self.allowed_providers


        else:
            allowed_providers = self.allowed_providers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "redirectUrl": redirect_url,
        })
        if state is not UNSET:
            field_dict["state"] = state
        if allowed_providers is not UNSET:
            field_dict["allowedProviders"] = allowed_providers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        redirect_url = d.pop("redirectUrl")

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_allowed_providers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_providers_type_0 = cast(list[str], data)

                return allowed_providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_providers = _parse_allowed_providers(d.pop("allowedProviders", UNSET))


        create_connect_session_body = cls(
            redirect_url=redirect_url,
            state=state,
            allowed_providers=allowed_providers,
        )


        create_connect_session_body.additional_properties = d
        return create_connect_session_body

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
