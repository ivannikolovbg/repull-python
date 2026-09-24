from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_migration_import_body_entities_item import RunMigrationImportBodyEntitiesItem
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="RunMigrationImportBody")



@_attrs_define
class RunMigrationImportBody:
    """ 
        Attributes:
            entities (list[RunMigrationImportBodyEntitiesItem] | Unset): Defaults to listings and reservations.
            since (datetime.datetime | Unset): Only reservations changed after this.
     """

    entities: list[RunMigrationImportBodyEntitiesItem] | Unset = UNSET
    since: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        entities: list[str] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.value
                entities.append(entities_item)



        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entities is not UNSET:
            field_dict["entities"] = entities
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _entities = d.pop("entities", UNSET)
        entities: list[RunMigrationImportBodyEntitiesItem] | Unset = UNSET
        if _entities is not UNSET:
            entities = []
            for entities_item_data in _entities:
                entities_item = RunMigrationImportBodyEntitiesItem(entities_item_data)



                entities.append(entities_item)


        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since,  Unset):
            since = UNSET
        else:
            since = isoparse(_since)




        run_migration_import_body = cls(
            entities=entities,
            since=since,
        )

        return run_migration_import_body

