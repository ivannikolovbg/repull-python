from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_connect_session_body_purpose import CreateConnectSessionBodyPurpose
from ..models.create_connect_session_body_scope_item import CreateConnectSessionBodyScopeItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_connect_session_body_copy import CreateConnectSessionBodyCopy
  from ..models.create_connect_session_body_workspace import CreateConnectSessionBodyWorkspace





T = TypeVar("T", bound="CreateConnectSessionBody")



@_attrs_define
class CreateConnectSessionBody:
    """ 
        Attributes:
            redirect_url (str): Where to send the user after they finish (or cancel). Status query params are appended.
            state (None | str | Unset): Opaque pass-through correlation token. Echoed back in the response.
            allowed_providers (list[str] | None | Unset): Optional whitelist of provider IDs the picker should expose. Omit
                to show every channel in the registry.
            locale (None | str | Unset): Optional UI language for the hosted Connect pages. Accepts any supported locale
                code (currently `en`, `fr`). When set it pins the language for the whole flow, overriding the workspace
                `default_language`. Unknown codes are ignored and the page falls back to the workspace default, then `Accept-
                Language`, then `en`. The end user can still override per-visit with a `?locale=` query param on the hosted
                page. Example: fr.
            purpose (CreateConnectSessionBodyPurpose | Unset): `migrate` starts a Repull Migrate session: the property
                manager connects their current PMS (or channel) and their data is copied into a new workspace of theirs, which
                you read with `X-Workspace-Id`. The hosted pages use migration wording, and after connecting they show the
                import's progress. Default: CreateConnectSessionBodyPurpose.CONNECT.
            workspace (CreateConnectSessionBodyWorkspace | Unset): Migrate only — the property manager being moved. Required
                unless you send `X-Workspace-Id` to reconnect an existing migration.
            copy (CreateConnectSessionBodyCopy | Unset): Migrate only — your wording for the hosted pages. Anything you
                leave out uses Repull's localized migration copy.
            scope (list[CreateConnectSessionBodyScopeItem] | Unset): Migrate only — what you want brought across, listed to
                the property manager before they connect.
     """

    redirect_url: str
    state: None | str | Unset = UNSET
    allowed_providers: list[str] | None | Unset = UNSET
    locale: None | str | Unset = UNSET
    purpose: CreateConnectSessionBodyPurpose | Unset = CreateConnectSessionBodyPurpose.CONNECT
    workspace: CreateConnectSessionBodyWorkspace | Unset = UNSET
    copy: CreateConnectSessionBodyCopy | Unset = UNSET
    scope: list[CreateConnectSessionBodyScopeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_connect_session_body_copy import CreateConnectSessionBodyCopy
        from ..models.create_connect_session_body_workspace import CreateConnectSessionBodyWorkspace
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

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value


        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        copy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy, Unset):
            copy = self.copy.to_dict()

        scope: list[str] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = []
            for scope_item_data in self.scope:
                scope_item = scope_item_data.value
                scope.append(scope_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "redirectUrl": redirect_url,
        })
        if state is not UNSET:
            field_dict["state"] = state
        if allowed_providers is not UNSET:
            field_dict["allowedProviders"] = allowed_providers
        if locale is not UNSET:
            field_dict["locale"] = locale
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if copy is not UNSET:
            field_dict["copy"] = copy
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_connect_session_body_copy import CreateConnectSessionBodyCopy
        from ..models.create_connect_session_body_workspace import CreateConnectSessionBodyWorkspace
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


        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))


        _purpose = d.pop("purpose", UNSET)
        purpose: CreateConnectSessionBodyPurpose | Unset
        if isinstance(_purpose,  Unset):
            purpose = UNSET
        else:
            purpose = CreateConnectSessionBodyPurpose(_purpose)




        _workspace = d.pop("workspace", UNSET)
        workspace: CreateConnectSessionBodyWorkspace | Unset
        if isinstance(_workspace,  Unset):
            workspace = UNSET
        else:
            workspace = CreateConnectSessionBodyWorkspace.from_dict(_workspace)




        _copy = d.pop("copy", UNSET)
        copy: CreateConnectSessionBodyCopy | Unset
        if isinstance(_copy,  Unset):
            copy = UNSET
        else:
            copy = CreateConnectSessionBodyCopy.from_dict(_copy)




        _scope = d.pop("scope", UNSET)
        scope: list[CreateConnectSessionBodyScopeItem] | Unset = UNSET
        if _scope is not UNSET:
            scope = []
            for scope_item_data in _scope:
                scope_item = CreateConnectSessionBodyScopeItem(scope_item_data)



                scope.append(scope_item)


        create_connect_session_body = cls(
            redirect_url=redirect_url,
            state=state,
            allowed_providers=allowed_providers,
            locale=locale,
            purpose=purpose,
            workspace=workspace,
            copy=copy,
            scope=scope,
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
