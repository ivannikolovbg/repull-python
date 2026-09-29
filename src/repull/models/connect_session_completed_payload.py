from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_session_completed_payload_purpose import ConnectSessionCompletedPayloadPurpose
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ConnectSessionCompletedPayload")



@_attrs_define
class ConnectSessionCompletedPayload:
    """ Payload for `connect.session.completed`. A user finished a Connect session, on any channel or PMS. Use `state` (your
    token from session creation) or `sessionId` to tie the connection to your own user; the account it names is keyed
    the same way as every other event's `account` block.

        Attributes:
            session_id (str | Unset):  Example: cs_abc123.
            state (None | str | Unset): The `state` you passed when creating the session. Example: user_8421.
            provider (None | str | Unset): Channel or PMS: airbnb, booking, booking_extranet, vrbo, plumguide, hostaway, …
                Example: vrbo.
            external_account_id (None | str | Unset): The provider's own account id — Airbnb host id, Booking.com hotel id,
                Vrbo account id, or the PMS account. Example: 36.
            connection_id (int | None | Unset): Repull connection id, when the account has one (the `X-Account-Id` value).
            purpose (ConnectSessionCompletedPayloadPurpose | Unset):
            completed_at (datetime.datetime | Unset):
     """

    session_id: str | Unset = UNSET
    state: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    connection_id: int | None | Unset = UNSET
    purpose: ConnectSessionCompletedPayloadPurpose | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        connection_id: int | None | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value


        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if state is not UNSET:
            field_dict["state"] = state
        if provider is not UNSET:
            field_dict["provider"] = provider
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId", UNSET)

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        def _parse_connection_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        _purpose = d.pop("purpose", UNSET)
        purpose: ConnectSessionCompletedPayloadPurpose | Unset
        if isinstance(_purpose,  Unset):
            purpose = UNSET
        else:
            purpose = ConnectSessionCompletedPayloadPurpose(_purpose)




        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at,  Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)




        connect_session_completed_payload = cls(
            session_id=session_id,
            state=state,
            provider=provider,
            external_account_id=external_account_id,
            connection_id=connection_id,
            purpose=purpose,
            completed_at=completed_at,
        )


        connect_session_completed_payload.additional_properties = d
        return connect_session_completed_payload

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
