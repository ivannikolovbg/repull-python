from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversation_message_status_changed_event_event import ConversationMessageStatusChangedEventEvent
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.conversation_message_status_changed_payload import ConversationMessageStatusChangedPayload
  from ..models.webhook_event_account_type_0 import WebhookEventAccountType0





T = TypeVar("T", bound="ConversationMessageStatusChangedEvent")



@_attrs_define
class ConversationMessageStatusChangedEvent:
    """ A message you sent was delivered or gave up after the send call returned. Update the message you show from `status`
    and `statusReason`.

        Attributes:
            event (ConversationMessageStatusChangedEventEvent): The event name. This field is `event`, not `type`.
            event_id (UUID): Stable across every delivery and replay of this logical event — dedupe on it.
            api_version (str):  Example: 2026-04.
            timestamp (datetime.datetime): When this delivery was built.
            data (ConversationMessageStatusChangedPayload): Payload for `conversation.message.status_changed`: a message you
                sent changed delivery status after the send call returned — a Vrbo reply accepted as `queued` (`202`) was
                delivered (`sent`) or gave up (`failed`).
            account (None | Unset | WebhookEventAccountType0): Which connected account produced this event. Null when it
                cannot be resolved — present-but-null rather than omitted, so a receiver can tell "unresolvable" from "an old
                event".
            workspace_id (int | Unset): The sub-workspace this event happened in. Present only on events from a sub-
                workspace your workspace opened (`POST /v1/connect` with `workspace`, or Repull Migrate); omitted on your own
                workspace's events. It is the same workspace as `workspaceId` on `POST /v1/connect` and `GET /v1/workspaces` and
                the `X-Workspace-Id` header, but those return it as a string (`"2042"`) while the event carries a JSON number
                (`2042`): compare as strings, e.g. `String(event.workspaceId) === workspace.workspaceId`. The UUID
                `data.workspaceId` on `account.created` / `account.disconnected` is a different identifier. Example: 2042.
     """

    event: ConversationMessageStatusChangedEventEvent
    event_id: UUID
    api_version: str
    timestamp: datetime.datetime
    data: ConversationMessageStatusChangedPayload
    account: None | Unset | WebhookEventAccountType0 = UNSET
    workspace_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_message_status_changed_payload import ConversationMessageStatusChangedPayload
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

        workspace_id = self.workspace_id


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
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_message_status_changed_payload import ConversationMessageStatusChangedPayload
        from ..models.webhook_event_account_type_0 import WebhookEventAccountType0
        d = dict(src_dict)
        event = ConversationMessageStatusChangedEventEvent(d.pop("event"))




        event_id = UUID(d.pop("eventId"))




        api_version = d.pop("apiVersion")

        timestamp = isoparse(d.pop("timestamp"))




        data = ConversationMessageStatusChangedPayload.from_dict(d.pop("data"))




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


        workspace_id = d.pop("workspaceId", UNSET)

        conversation_message_status_changed_event = cls(
            event=event,
            event_id=event_id,
            api_version=api_version,
            timestamp=timestamp,
            data=data,
            account=account,
            workspace_id=workspace_id,
        )


        conversation_message_status_changed_event.additional_properties = d
        return conversation_message_status_changed_event

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
