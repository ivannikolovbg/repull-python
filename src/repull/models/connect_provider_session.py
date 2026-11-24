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






T = TypeVar("T", bound="ConnectProviderSession")



@_attrs_define
class ConnectProviderSession:
    """ A hosted Connect session for one provider (`POST /v1/connect/{provider}`). Send the user to `url`; every return to
    your `redirectUrl` carries `status`, `sessionId` and your `state`.

        Attributes:
            url (str): The hosted page to send the user to. Example:
                https://connect.repull.dev/cs_8gQrT2v9k3M4nLp7wJxYzAbCdEfGhIjKlMnOp.
            provider (str):  Example: airbnb.
            session_id (str): Also sent back on the redirect (`sessionId=`), in the popup message and in
                `connect.session.completed`. Example: cs_8gQrT2v9k3M4nLp7wJxYzAbCdEfGhIjKlMnOp.
            expires_at (datetime.datetime):
            state (None | str | Unset): Your `state` from the request, echoed; `null` when you sent none.
            workspace_id (str | Unset): PriceLabs only, when the request opened a sub-workspace (`workspace.name`). Example:
                1204.
     """

    url: str
    provider: str
    session_id: str
    expires_at: datetime.datetime
    state: None | str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        provider = self.provider

        session_id = self.session_id

        expires_at = self.expires_at.isoformat()

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        workspace_id = self.workspace_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
            "provider": provider,
            "sessionId": session_id,
            "expiresAt": expires_at,
        })
        if state is not UNSET:
            field_dict["state"] = state
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        provider = d.pop("provider")

        session_id = d.pop("sessionId")

        expires_at = isoparse(d.pop("expiresAt"))




        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        workspace_id = d.pop("workspaceId", UNSET)

        connect_provider_session = cls(
            url=url,
            provider=provider,
            session_id=session_id,
            expires_at=expires_at,
            state=state,
            workspace_id=workspace_id,
        )


        connect_provider_session.additional_properties = d
        return connect_provider_session

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
