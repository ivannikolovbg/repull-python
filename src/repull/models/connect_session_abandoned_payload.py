from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_session_abandoned_payload_reason import ConnectSessionAbandonedPayloadReason
from ..models.connect_session_abandoned_payload_status import ConnectSessionAbandonedPayloadStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ConnectSessionAbandonedPayload")



@_attrs_define
class ConnectSessionAbandonedPayload:
    """ Payload for `connect.session.abandoned`. A user opened a Connect session and never finished it — the link ran out,
    or the account was connected but its rooms were never mapped. Use `state` or `sessionId` to find your user, `reason`
    and `nextStep` to decide what to send them (usually a new Connect link). Sent once per session, only for sessions
    opened in the last 7 days.

        Attributes:
            session_id (str | Unset):  Example: cs_abc123.
            state (None | str | Unset): The `state` you passed when creating the session. Example: user_8421.
            provider (None | str | Unset): Channel or PMS the user picked: airbnb, booking, booking_extranet, vrbo,
                hostaway, … Example: booking.
            status (ConnectSessionAbandonedPayloadStatus | Unset): `expired`: the link ran out before the user finished.
                `awaiting_room_mapping`: the account is connected; its rooms were never matched to listings.
            reason (ConnectSessionAbandonedPayloadReason | Unset): `not_finished`: opened and left. `credentials_rejected`:
                the provider refused the key or token the user entered. `provider_approval_pending`: Booking.com never confirmed
                the property in the Extranet. `mapping_not_finished`: connected, rooms not mapped. `failed`: another error, see
                `lastErrorCode`.
            last_error_code (None | str | Unset): The last error the user hit on the Connect page, e.g.
                `invalid_credentials`, `awaiting_designation`. Example: awaiting_designation.
            external_account_id (None | str | Unset): Booking.com: the Hotel ID the user entered while waiting for the
                Extranet approval. Example: 17168363.
            next_step (str | Unset): What to tell the user, in plain English.
            created_at (datetime.datetime | Unset):
            last_activity_at (datetime.datetime | Unset):
     """

    session_id: str | Unset = UNSET
    state: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    status: ConnectSessionAbandonedPayloadStatus | Unset = UNSET
    reason: ConnectSessionAbandonedPayloadReason | Unset = UNSET
    last_error_code: None | str | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    next_step: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    last_activity_at: datetime.datetime | Unset = UNSET
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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value


        last_error_code: None | str | Unset
        if isinstance(self.last_error_code, Unset):
            last_error_code = UNSET
        else:
            last_error_code = self.last_error_code

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        next_step = self.next_step

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        last_activity_at: str | Unset = UNSET
        if not isinstance(self.last_activity_at, Unset):
            last_activity_at = self.last_activity_at.isoformat()


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
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if last_error_code is not UNSET:
            field_dict["lastErrorCode"] = last_error_code
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if next_step is not UNSET:
            field_dict["nextStep"] = next_step
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at

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


        _status = d.pop("status", UNSET)
        status: ConnectSessionAbandonedPayloadStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConnectSessionAbandonedPayloadStatus(_status)




        _reason = d.pop("reason", UNSET)
        reason: ConnectSessionAbandonedPayloadReason | Unset
        if isinstance(_reason,  Unset):
            reason = UNSET
        else:
            reason = ConnectSessionAbandonedPayloadReason(_reason)




        def _parse_last_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error_code = _parse_last_error_code(d.pop("lastErrorCode", UNSET))


        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        next_step = d.pop("nextStep", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _last_activity_at = d.pop("lastActivityAt", UNSET)
        last_activity_at: datetime.datetime | Unset
        if isinstance(_last_activity_at,  Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = isoparse(_last_activity_at)




        connect_session_abandoned_payload = cls(
            session_id=session_id,
            state=state,
            provider=provider,
            status=status,
            reason=reason,
            last_error_code=last_error_code,
            external_account_id=external_account_id,
            next_step=next_step,
            created_at=created_at,
            last_activity_at=last_activity_at,
        )


        connect_session_abandoned_payload.additional_properties = d
        return connect_session_abandoned_payload

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
