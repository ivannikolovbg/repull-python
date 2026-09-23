from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_request_updated_event_event import ReservationRequestUpdatedEventEvent
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.reservation_request_updated_payload import ReservationRequestUpdatedPayload
  from ..models.webhook_event_account_type_0 import WebhookEventAccountType0





T = TypeVar("T", bound="ReservationRequestUpdatedEvent")



@_attrs_define
class ReservationRequestUpdatedEvent:
    """ 
        Attributes:
            event (ReservationRequestUpdatedEventEvent): The event name. This field is `event`, not `type`.
            event_id (UUID): Stable across every delivery and replay of this logical event — dedupe on it.
            api_version (str):  Example: 2026-04.
            timestamp (datetime.datetime): When this delivery was built.
            data (ReservationRequestUpdatedPayload): Payload for `reservation.request.updated`. A booking request stopped
                waiting on the host. `requestStatus` says how; `data.object` is the reservation after the change (`status`
                `confirmed` once accepted, `cancelled` otherwise). An accepted request also fires `reservation.created`. Fires
                when the channel reports the outcome, whoever acted — the API, a connected app or the channel's own app.
            account (None | Unset | WebhookEventAccountType0): Which connected account produced this event. Null when it
                cannot be resolved — present-but-null rather than omitted, so a receiver can tell "unresolvable" from "an old
                event".
     """

    event: ReservationRequestUpdatedEventEvent
    event_id: UUID
    api_version: str
    timestamp: datetime.datetime
    data: ReservationRequestUpdatedPayload
    account: None | Unset | WebhookEventAccountType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_request_updated_payload import ReservationRequestUpdatedPayload
        from ..models.webhook_event_account_type_0 import WebhookEventAccountType0
        event = self.event.value

        event_id = str(self.event_id)

        api_version = self.api_version

        timestamp = self.timestamp.isoformat()

        data = self.data.to_dict()

        account: dict[str, Any] | None | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        elif isinstance(self.account, WebhookEventAccountType0):
            account = self.account.to_dict()
        else:
            account = self.account


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "event": event,
            "eventId": event_id,
            "apiVersion": api_version,
            "timestamp": timestamp,
            "data": data,
        })
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_request_updated_payload import ReservationRequestUpdatedPayload
        from ..models.webhook_event_account_type_0 import WebhookEventAccountType0
        d = dict(src_dict)
        event = ReservationRequestUpdatedEventEvent(d.pop("event"))




        event_id = UUID(d.pop("eventId"))




        api_version = d.pop("apiVersion")

        timestamp = isoparse(d.pop("timestamp"))




        data = ReservationRequestUpdatedPayload.from_dict(d.pop("data"))




        def _parse_account(data: object) -> None | Unset | WebhookEventAccountType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_event_account_type_0 = WebhookEventAccountType0.from_dict(data)



                return componentsschemas_webhook_event_account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookEventAccountType0, data)

        account = _parse_account(d.pop("account", UNSET))


        reservation_request_updated_event = cls(
            event=event,
            event_id=event_id,
            api_version=api_version,
            timestamp=timestamp,
            data=data,
            account=account,
        )


        reservation_request_updated_event.additional_properties = d
        return reservation_request_updated_event

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
