from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_calendar_access_changed_payload_provider import AccountCalendarAccessChangedPayloadProvider
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.vrbo_calendar_access import VrboCalendarAccess





T = TypeVar("T", bound="AccountCalendarAccessChangedPayload")



@_attrs_define
class AccountCalendarAccessChangedPayload:
    """ 
        Attributes:
            workspace_id (int):
            provider (AccountCalendarAccessChangedPayloadProvider):
            account_id (None | str): Vrbo's account number (`accounts[].externalAccountId` on `GET /v1/connect/vrbo-login`).
            connection_id (int | None): The workspace's Vrbo connection record.
            calendar (VrboCalendarAccess): Whether another tool manages a Vrbo account's calendar. Vrbo reports it per
                account; Repull asks when the account connects and once a day. While `managedBy` is set, Vrbo refuses price and
                availability changes from anyone else, so calendar sync is off for every unit of the account and turning it on
                returns `409 calendar_managed_elsewhere`. Bookings and messages keep working.
            changed_at (datetime.datetime):
     """

    workspace_id: int
    provider: AccountCalendarAccessChangedPayloadProvider
    account_id: None | str
    connection_id: int | None
    calendar: VrboCalendarAccess
    changed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vrbo_calendar_access import VrboCalendarAccess
        workspace_id = self.workspace_id

        provider = self.provider.value

        account_id: None | str
        account_id = self.account_id

        connection_id: int | None
        connection_id = self.connection_id

        calendar = self.calendar.to_dict()

        changed_at = self.changed_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workspaceId": workspace_id,
            "provider": provider,
            "accountId": account_id,
            "connectionId": connection_id,
            "calendar": calendar,
            "changedAt": changed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vrbo_calendar_access import VrboCalendarAccess
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        provider = AccountCalendarAccessChangedPayloadProvider(d.pop("provider"))




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


        calendar = VrboCalendarAccess.from_dict(d.pop("calendar"))




        changed_at = isoparse(d.pop("changedAt"))




        account_calendar_access_changed_payload = cls(
            workspace_id=workspace_id,
            provider=provider,
            account_id=account_id,
            connection_id=connection_id,
            calendar=calendar,
            changed_at=changed_at,
        )


        account_calendar_access_changed_payload.additional_properties = d
        return account_calendar_access_changed_payload

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
