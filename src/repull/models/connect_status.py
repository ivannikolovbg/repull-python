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





T = TypeVar("T", bound="ConnectStatus")



@_attrs_define
class ConnectStatus:
    """ Connection status response for a single provider. When `connected` is false, all other fields except `provider` and
    `host` may be omitted, and `host` is null.

        Attributes:
            connected (bool | Unset):  Example: True.
            provider (str | Unset):  Example: airbnb.
            id (int | Unset): Repull-side connection ID. Stable across token refreshes. Example: 3.
            status (ConnectStatusStatus | Unset):  Example: active.
            external_account_id (None | str | Unset): Provider-side account ID (e.g. the Airbnb host ID). Example: 23998907.
            created_at (datetime.datetime | Unset):
            host (ConnectHost | None | Unset): Host metadata, populated for Airbnb when the host row exists. Null for other
                providers (per-provider enrichment is incremental).
     """

    connected: bool | Unset = UNSET
    provider: str | Unset = UNSET
    id: int | Unset = UNSET
    status: ConnectStatusStatus | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    host: ConnectHost | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_host import ConnectHost
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_host import ConnectHost
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


        connect_status = cls(
            connected=connected,
            provider=provider,
            id=id,
            status=status,
            external_account_id=external_account_id,
            created_at=created_at,
            host=host,
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
