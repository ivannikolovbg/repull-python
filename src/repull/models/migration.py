from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.migration_state import MigrationState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.migration_connections_item import MigrationConnectionsItem
  from ..models.migration_counts import MigrationCounts





T = TypeVar("T", bound="Migration")



@_attrs_define
class Migration:
    """ One migration: a property manager moved through Repull Migrate, living in its own workspace.

        Attributes:
            workspace_id (str): Pass as `X-Workspace-Id` to read this property manager's listings, reservations and
                conversations through the regular endpoints. Example: 1204.
            name (str):  Example: Seaside Rentals.
            state (MigrationState): `awaiting_connection` — not connected yet. `importing` — the first import is running.
                `imported` — data is in and kept fresh until cutover. `failed` — the last import failed (see
                `connections[].import.error`). `cut_over` — the source was disconnected. `deactivated` — the migration was
                deleted.
            connections (list[MigrationConnectionsItem]):
            counts (MigrationCounts):
            external_ref (None | str | Unset): Your own id for this property manager, as sent when the migration was
                created.
            created_at (datetime.datetime | Unset):
            cutover_at (datetime.datetime | None | Unset):
     """

    workspace_id: str
    name: str
    state: MigrationState
    connections: list[MigrationConnectionsItem]
    counts: MigrationCounts
    external_ref: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    cutover_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_connections_item import MigrationConnectionsItem
        from ..models.migration_counts import MigrationCounts
        workspace_id = self.workspace_id

        name = self.name

        state = self.state.value

        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)



        counts = self.counts.to_dict()

        external_ref: None | str | Unset
        if isinstance(self.external_ref, Unset):
            external_ref = UNSET
        else:
            external_ref = self.external_ref

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        cutover_at: None | str | Unset
        if isinstance(self.cutover_at, Unset):
            cutover_at = UNSET
        elif isinstance(self.cutover_at, datetime.datetime):
            cutover_at = self.cutover_at.isoformat()
        else:
            cutover_at = self.cutover_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workspaceId": workspace_id,
            "name": name,
            "state": state,
            "connections": connections,
            "counts": counts,
        })
        if external_ref is not UNSET:
            field_dict["externalRef"] = external_ref
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if cutover_at is not UNSET:
            field_dict["cutoverAt"] = cutover_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_connections_item import MigrationConnectionsItem
        from ..models.migration_counts import MigrationCounts
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        state = MigrationState(d.pop("state"))




        connections = []
        _connections = d.pop("connections")
        for connections_item_data in (_connections):
            connections_item = MigrationConnectionsItem.from_dict(connections_item_data)



            connections.append(connections_item)


        counts = MigrationCounts.from_dict(d.pop("counts"))




        def _parse_external_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_ref = _parse_external_ref(d.pop("externalRef", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        def _parse_cutover_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cutover_at_type_0 = isoparse(data)



                return cutover_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cutover_at = _parse_cutover_at(d.pop("cutoverAt", UNSET))


        migration = cls(
            workspace_id=workspace_id,
            name=name,
            state=state,
            connections=connections,
            counts=counts,
            external_ref=external_ref,
            created_at=created_at,
            cutover_at=cutover_at,
        )


        migration.additional_properties = d
        return migration

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
