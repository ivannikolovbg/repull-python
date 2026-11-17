from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_notifications_missing_payload_provider import AccountNotificationsMissingPayloadProvider
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.vrbo_notifications import VrboNotifications





T = TypeVar("T", bound="AccountNotificationsMissingPayload")



@_attrs_define
class AccountNotificationsMissingPayload:
    """ Payload for `account.notifications_missing`: a Vrbo account had new guest messages and no notification email arrived
    for them.

        Attributes:
            workspace_id (int):
            provider (AccountNotificationsMissingPayloadProvider):
            account_id (None | str): Vrbo's account number (`accounts[].externalAccountId` on `GET /v1/connect/vrbo-login`).
            connection_id (int | None): The workspace's Vrbo connection record.
            notifications (VrboNotifications): Whether Vrbo's notification emails for this account reach Repull. Each one
                brings a new guest message or booking in within about a minute; without them Repull relies on its scheduled
                check, which is slower.
            detected_at (datetime.datetime):
            docs_url (str | Unset):  Example: https://repull.dev/docs/channels/vrbo/notifications.
     """

    workspace_id: int
    provider: AccountNotificationsMissingPayloadProvider
    account_id: None | str
    connection_id: int | None
    notifications: VrboNotifications
    detected_at: datetime.datetime
    docs_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vrbo_notifications import VrboNotifications
        workspace_id = self.workspace_id

        provider = self.provider.value

        account_id: None | str
        account_id = self.account_id

        connection_id: int | None
        connection_id = self.connection_id

        notifications = self.notifications.to_dict()

        detected_at = self.detected_at.isoformat()

        docs_url = self.docs_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workspaceId": workspace_id,
            "provider": provider,
            "accountId": account_id,
            "connectionId": connection_id,
            "notifications": notifications,
            "detectedAt": detected_at,
        })
        if docs_url is not UNSET:
            field_dict["docsUrl"] = docs_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vrbo_notifications import VrboNotifications
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        provider = AccountNotificationsMissingPayloadProvider(d.pop("provider"))




        def _parse_account_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_id = _parse_account_id(d.pop("accountId"))


        def _parse_connection_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        connection_id = _parse_connection_id(d.pop("connectionId"))


        notifications = VrboNotifications.from_dict(d.pop("notifications"))




        detected_at = isoparse(d.pop("detectedAt"))




        docs_url = d.pop("docsUrl", UNSET)

        account_notifications_missing_payload = cls(
            workspace_id=workspace_id,
            provider=provider,
            account_id=account_id,
            connection_id=connection_id,
            notifications=notifications,
            detected_at=detected_at,
            docs_url=docs_url,
        )


        account_notifications_missing_payload.additional_properties = d
        return account_notifications_missing_payload

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
