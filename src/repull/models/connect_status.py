from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_status_status import ConnectStatusStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.connect_host import ConnectHost
  from ..models.connect_status_accounts_item import ConnectStatusAccountsItem
  from ..models.connect_status_capabilities import ConnectStatusCapabilities
  from ..models.connect_status_data_freshness import ConnectStatusDataFreshness
  from ..models.connection_action import ConnectionAction
  from ..models.pms_write_policy import PmsWritePolicy





T = TypeVar("T", bound="ConnectStatus")



@_attrs_define
class ConnectStatus:
    """ Connection status response for a single provider. When `connected` is false, all other fields except `provider` and
    `host` may be omitted, and `host` is null.

        Attributes:
            connected (bool | Unset):  Example: True.
            provider (str | Unset):  Example: airbnb.
            id (str | Unset): Repull-side connection ID. Stable across token refreshes. Example: 3.
            status (ConnectStatusStatus | Unset):  Example: active.
            external_account_id (None | str | Unset): Provider-side account ID (e.g. the Airbnb host ID). Example: 10000001.
            created_at (datetime.datetime | Unset):
            host (ConnectHost | None | Unset): Host metadata, populated for Airbnb when the host row exists. Null for other
                providers (per-provider enrichment is incremental).
            accounts (list[ConnectStatusAccountsItem] | Unset): Airbnb: every Airbnb account this workspace has connected,
                including ones since disconnected. Pass `externalAccountId` as `accountId` to `DELETE /v1/connect/airbnb` to
                disconnect one account. Vrbo (`GET /v1/connect/vrbo-login`): every signed-in Vrbo account, each with
                `accessType` and `import` (a `VrboImportStatus`), plus a top-level `dataFreshness`.
            write_policy (PmsWritePolicy | Unset): What the app may change in a connected PMS. Hotel PMSs (Cloudbeds, Mews)
                start with every `calendar` switch off, because the PMS owns its room inventory; every other PMS starts with
                everything on. Reading from the PMS is never affected. Example: {'calendar': {'availability': False, 'rates':
                True, 'restrictions': False}, 'reservations': {'website': True, 'dashboard': True, 'api': True}}.
            capabilities (ConnectStatusCapabilities | Unset): PMS providers only. `reservations`: which reservation writes
                the API performs on this connection's listings — the connector's support combined with `writePolicy`. When
                `connected` is false, what the connector supports once connected.
            data_freshness (ConnectStatusDataFreshness | Unset): Vrbo only: the same freshness envelope the Airbnb read
                endpoints return, per account and in aggregate. Its reason is never_synced until a mapping is confirmed and
                importing while upcoming bookings come in.
            action (ConnectionAction | None | Unset): Smoobu only: set to `{ required: true, reason: "reauth_required",
                message }` when the connection still uses a legacy single API key, which Smoobu stops accepting on October 31,
                2026. `null` once it is on an API key + secret.
            fix_url (None | str | Unset): Smoobu only: durable link to the hosted Smoobu form where the host pastes a new
                API key + secret. Submitting it updates this same connection (`id` unchanged). Present only when
                `action.required` is true.
     """

    connected: bool | Unset = UNSET
    provider: str | Unset = UNSET
    id: str | Unset = UNSET
    status: ConnectStatusStatus | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    host: ConnectHost | None | Unset = UNSET
    accounts: list[ConnectStatusAccountsItem] | Unset = UNSET
    write_policy: PmsWritePolicy | Unset = UNSET
    capabilities: ConnectStatusCapabilities | Unset = UNSET
    data_freshness: ConnectStatusDataFreshness | Unset = UNSET
    action: ConnectionAction | None | Unset = UNSET
    fix_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_host import ConnectHost
        from ..models.connect_status_accounts_item import ConnectStatusAccountsItem
        from ..models.connect_status_capabilities import ConnectStatusCapabilities
        from ..models.connect_status_data_freshness import ConnectStatusDataFreshness
        from ..models.connection_action import ConnectionAction
        from ..models.pms_write_policy import PmsWritePolicy
        connected = self.connected

        provider = self.provider

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        host: dict[str, Any] | None | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        elif isinstance(self.host, ConnectHost):
            host = self.host.to_dict()
        else:
            host = self.host

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)



        write_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.write_policy, Unset):
            write_policy = self.write_policy.to_dict()

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        data_freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.to_dict()

        action: dict[str, Any] | None | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, ConnectionAction):
            action = self.action.to_dict()
        else:
            action = self.action

        fix_url: None | str | Unset
        if isinstance(self.fix_url, Unset):
            fix_url = UNSET
        else:
            fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connected is not UNSET:
            field_dict["connected"] = connected
        if provider is not UNSET:
            field_dict["provider"] = provider
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if host is not UNSET:
            field_dict["host"] = host
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if write_policy is not UNSET:
            field_dict["writePolicy"] = write_policy
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if data_freshness is not UNSET:
            field_dict["dataFreshness"] = data_freshness
        if action is not UNSET:
            field_dict["action"] = action
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_host import ConnectHost
        from ..models.connect_status_accounts_item import ConnectStatusAccountsItem
        from ..models.connect_status_capabilities import ConnectStatusCapabilities
        from ..models.connect_status_data_freshness import ConnectStatusDataFreshness
        from ..models.connection_action import ConnectionAction
        from ..models.pms_write_policy import PmsWritePolicy
        d = dict(src_dict)
        connected = d.pop("connected", UNSET)

        provider = d.pop("provider", UNSET)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: ConnectStatusStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConnectStatusStatus(_status)




        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        def _parse_host(data: object) -> ConnectHost | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                host_type_1 = ConnectHost.from_dict(data)



                return host_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectHost | None | Unset, data)

        host = _parse_host(d.pop("host", UNSET))


        _accounts = d.pop("accounts", UNSET)
        accounts: list[ConnectStatusAccountsItem] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = ConnectStatusAccountsItem.from_dict(accounts_item_data)



                accounts.append(accounts_item)


        _write_policy = d.pop("writePolicy", UNSET)
        write_policy: PmsWritePolicy | Unset
        if isinstance(_write_policy,  Unset):
            write_policy = UNSET
        else:
            write_policy = PmsWritePolicy.from_dict(_write_policy)




        _capabilities = d.pop("capabilities", UNSET)
        capabilities: ConnectStatusCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = ConnectStatusCapabilities.from_dict(_capabilities)




        _data_freshness = d.pop("dataFreshness", UNSET)
        data_freshness: ConnectStatusDataFreshness | Unset
        if isinstance(_data_freshness,  Unset):
            data_freshness = UNSET
        else:
            data_freshness = ConnectStatusDataFreshness.from_dict(_data_freshness)




        def _parse_action(data: object) -> ConnectionAction | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_1 = ConnectionAction.from_dict(data)



                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionAction | None | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


        def _parse_fix_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fix_url = _parse_fix_url(d.pop("fixUrl", UNSET))


        connect_status = cls(
            connected=connected,
            provider=provider,
            id=id,
            status=status,
            external_account_id=external_account_id,
            created_at=created_at,
            host=host,
            accounts=accounts,
            write_policy=write_policy,
            capabilities=capabilities,
            data_freshness=data_freshness,
            action=action,
            fix_url=fix_url,
        )


        connect_status.additional_properties = d
        return connect_status

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
