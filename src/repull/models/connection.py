from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_access_type import ConnectionAccessType
from ..models.connection_scope import ConnectionScope
from ..models.connection_status import ConnectionStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.account_import import AccountImport
  from ..models.app_connection_health import AppConnectionHealth
  from ..models.connect_host import ConnectHost
  from ..models.connection_action import ConnectionAction





T = TypeVar("T", bound="Connection")



@_attrs_define
class Connection:
    """ 
        Attributes:
            id (str | Unset):
            provider (str | Unset):  Example: hostaway.
            status (ConnectionStatus | Unset): `active` — connected and working. `pending` — still settling.
                `needs_permissions` — connected but the host must grant more access before it works (see `action`/`fixUrl`). An
                `active` connection can also carry an `action` (e.g. a Smoobu legacy API key that must be replaced with a key +
                secret before October 31, 2026). `error` — the last operation failed. `disconnected` — revoked or superseded.
                Example: active.
            external_account_id (None | str | Unset): The platform's own account id: Airbnb host id; Booking.com hotel id
                (`booking`); the Booking.com account id behind the Extranet login (`booking_extranet`); Vrbo's account id
                (`vrbo`); the PMS's own account or company id. `null` when the platform id is not known yet (a Vrbo sign-in
                before its account id is captured, a PMS that does not expose one); never a Repull id. Use `id` for our record.
                Example: 20123456.
            access_type (ConnectionAccessType | None | Unset): What this connection may do: `read_only`, `messaging` or
                `full_access` (see `ConnectionAccessType` for the meaning per provider). Airbnb: the tier of the host in
                `externalAccountId`. `null` when unknown.
            created_at (datetime.datetime | Unset):
            host (ConnectHost | None | Unset): Host metadata for the linked account. Currently populated for Airbnb only;
                null for other providers.
            action (ConnectionAction | None | Unset): Set when the host must do something before the connection works (e.g.
                grant the invited Booking.com Extranet user full access), or has units still to map (`reason: needs_mapping` —
                Booking.com Extranet rooms, Vrbo units; `required` is false when only some Vrbo units are left). `null` when no
                action is pending.
            fix_url (None | str | Unset): Durable link that reopens the hosted Connect flow bound to this account on the fix
                screen — send the host here to resolve `action`. For `needs_mapping` it opens the unit mapping directly (no new
                sign-in). Present whenever `action` is set; `null` otherwise.
            import_ (AccountImport | None | Unset): The account's latest import — `status: running` while the first sync (or
                a later one) is going, then `completed` or `failed`. `null` when no import has been recorded. The same run is
                announced by the `account.import.*` webhooks; the history is on `GET /v1/connections/{id}/imports`.
            scope (ConnectionScope | Unset): Apps (`pricelabs`) only. `workspace`: every listing of the workspace, including
                listings added later. `listings`: only `listingIds`.
            listing_ids (list[str] | None | Unset): Apps only: the listings a `listings`-scoped connection covers; `null`
                for `workspace`.
            listing_count (int | Unset): Apps only: listings the connection covers now. Example: 12.
            key_masked (str | Unset): Apps only: the key the app uses, masked. The key itself is shown once, when created.
                Example: sk_live_4eB3...XYZw.
            label (None | str | Unset): Apps only: the name given to the key.
            disconnected_at (datetime.datetime | None | Unset): Apps only: when the connection was revoked.
            health (AppConnectionHealth | None | Unset): Apps only: how the app is doing on this connection. `null` once
                disconnected.
     """

    id: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: ConnectionStatus | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    access_type: ConnectionAccessType | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    host: ConnectHost | None | Unset = UNSET
    action: ConnectionAction | None | Unset = UNSET
    fix_url: None | str | Unset = UNSET
    import_: AccountImport | None | Unset = UNSET
    scope: ConnectionScope | Unset = UNSET
    listing_ids: list[str] | None | Unset = UNSET
    listing_count: int | Unset = UNSET
    key_masked: str | Unset = UNSET
    label: None | str | Unset = UNSET
    disconnected_at: datetime.datetime | None | Unset = UNSET
    health: AppConnectionHealth | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_import import AccountImport
        from ..models.app_connection_health import AppConnectionHealth
        from ..models.connect_host import ConnectHost
        from ..models.connection_action import ConnectionAction
        id = self.id

        provider = self.provider

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        access_type: None | str | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        elif isinstance(self.access_type, ConnectionAccessType):
            access_type = self.access_type.value
        else:
            access_type = self.access_type

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

        import_: dict[str, Any] | None | Unset
        if isinstance(self.import_, Unset):
            import_ = UNSET
        elif isinstance(self.import_, AccountImport):
            import_ = self.import_.to_dict()
        else:
            import_ = self.import_

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value


        listing_ids: list[str] | None | Unset
        if isinstance(self.listing_ids, Unset):
            listing_ids = UNSET
        elif isinstance(self.listing_ids, list):
            listing_ids = self.listing_ids


        else:
            listing_ids = self.listing_ids

        listing_count = self.listing_count

        key_masked = self.key_masked

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        disconnected_at: None | str | Unset
        if isinstance(self.disconnected_at, Unset):
            disconnected_at = UNSET
        elif isinstance(self.disconnected_at, datetime.datetime):
            disconnected_at = self.disconnected_at.isoformat()
        else:
            disconnected_at = self.disconnected_at

        health: dict[str, Any] | None | Unset
        if isinstance(self.health, Unset):
            health = UNSET
        elif isinstance(self.health, AppConnectionHealth):
            health = self.health.to_dict()
        else:
            health = self.health


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if host is not UNSET:
            field_dict["host"] = host
        if action is not UNSET:
            field_dict["action"] = action
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url
        if import_ is not UNSET:
            field_dict["import"] = import_
        if scope is not UNSET:
            field_dict["scope"] = scope
        if listing_ids is not UNSET:
            field_dict["listingIds"] = listing_ids
        if listing_count is not UNSET:
            field_dict["listingCount"] = listing_count
        if key_masked is not UNSET:
            field_dict["keyMasked"] = key_masked
        if label is not UNSET:
            field_dict["label"] = label
        if disconnected_at is not UNSET:
            field_dict["disconnectedAt"] = disconnected_at
        if health is not UNSET:
            field_dict["health"] = health

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_import import AccountImport
        from ..models.app_connection_health import AppConnectionHealth
        from ..models.connect_host import ConnectHost
        from ..models.connection_action import ConnectionAction
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        provider = d.pop("provider", UNSET)

        _status = d.pop("status", UNSET)
        status: ConnectionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConnectionStatus(_status)




        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        def _parse_access_type(data: object) -> ConnectionAccessType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_1 = ConnectionAccessType(data)



                return access_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionAccessType | None | Unset, data)

        access_type = _parse_access_type(d.pop("accessType", UNSET))


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


        def _parse_import_(data: object) -> AccountImport | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                import_type_1 = AccountImport.from_dict(data)



                return import_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountImport | None | Unset, data)

        import_ = _parse_import_(d.pop("import", UNSET))


        _scope = d.pop("scope", UNSET)
        scope: ConnectionScope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = ConnectionScope(_scope)




        def _parse_listing_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                listing_ids_type_0 = cast(list[str], data)

                return listing_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        listing_ids = _parse_listing_ids(d.pop("listingIds", UNSET))


        listing_count = d.pop("listingCount", UNSET)

        key_masked = d.pop("keyMasked", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_disconnected_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disconnected_at_type_0 = isoparse(data)



                return disconnected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        disconnected_at = _parse_disconnected_at(d.pop("disconnectedAt", UNSET))


        def _parse_health(data: object) -> AppConnectionHealth | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_type_1 = AppConnectionHealth.from_dict(data)



                return health_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppConnectionHealth | None | Unset, data)

        health = _parse_health(d.pop("health", UNSET))


        connection = cls(
            id=id,
            provider=provider,
            status=status,
            external_account_id=external_account_id,
            access_type=access_type,
            created_at=created_at,
            host=host,
            action=action,
            fix_url=fix_url,
            import_=import_,
            scope=scope,
            listing_ids=listing_ids,
            listing_count=listing_count,
            key_masked=key_masked,
            label=label,
            disconnected_at=disconnected_at,
            health=health,
        )


        connection.additional_properties = d
        return connection

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
