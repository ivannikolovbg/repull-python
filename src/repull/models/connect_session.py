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






T = TypeVar("T", bound="ConnectSession")



@_attrs_define
class ConnectSession:
    """ A multi-channel Connect picker session. The `url` is the hosted picker page on connect.repull.dev — redirect the
    host to it, they pick a channel, and the picker takes them through the per-provider flow before redirecting back to
    the original `redirectUrl`.

        Attributes:
            session_id (str):  Example: cs_8gQrT2v9k3M4nLp7wJxYzAbCdEfGhIjKlMnOp.
            url (str):  Example: https://connect.repull.dev/cs_8gQrT2v9k3M4nLp7wJxYzAbCdEfGhIjKlMnOp.
            expires_at (datetime.datetime):
            state (None | str | Unset): Echoed back from the request body for SDK consumers that pass an opaque correlation
                token.
     """

    session_id: str
    url: str
    expires_at: datetime.datetime
    state: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        url = self.url

        expires_at = self.expires_at.isoformat()

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessionId": session_id,
            "url": url,
            "expiresAt": expires_at,
        })
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId")

        url = d.pop("url")

        expires_at = isoparse(d.pop("expiresAt"))




        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        connect_session = cls(
            session_id=session_id,
            url=url,
            expires_at=expires_at,
            state=state,
        )


        connect_session.additional_properties = d
        return connect_session

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
