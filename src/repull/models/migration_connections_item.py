from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.migration_import_run import MigrationImportRun





T = TypeVar("T", bound="MigrationConnectionsItem")



@_attrs_define
class MigrationConnectionsItem:
    """ 
        Attributes:
            id (str | Unset):
            provider (str | Unset):  Example: guesty.
            status (str | Unset):  Example: active.
            connected_at (datetime.datetime | Unset):
            last_polled_at (datetime.datetime | None | Unset):
            import_ (MigrationImportRun | None | Unset): The last import run, or null before the first one (and for
                channels, which sync on their own schedule).
     """

    id: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    connected_at: datetime.datetime | Unset = UNSET
    last_polled_at: datetime.datetime | None | Unset = UNSET
    import_: MigrationImportRun | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_import_run import MigrationImportRun
        id = self.id

        provider = self.provider

        status = self.status

        connected_at: str | Unset = UNSET
        if not isinstance(self.connected_at, Unset):
            connected_at = self.connected_at.isoformat()

        last_polled_at: None | str | Unset
        if isinstance(self.last_polled_at, Unset):
            last_polled_at = UNSET
        elif isinstance(self.last_polled_at, datetime.datetime):
            last_polled_at = self.last_polled_at.isoformat()
        else:
            last_polled_at = self.last_polled_at

        import_: dict[str, Any] | None | Unset
        if isinstance(self.import_, Unset):
            import_ = UNSET
        elif isinstance(self.import_, MigrationImportRun):
            import_ = self.import_.to_dict()
        else:
            import_ = self.import_


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
        if connected_at is not UNSET:
            field_dict["connectedAt"] = connected_at
        if last_polled_at is not UNSET:
            field_dict["lastPolledAt"] = last_polled_at
        if import_ is not UNSET:
            field_dict["import"] = import_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_import_run import MigrationImportRun
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        _connected_at = d.pop("connectedAt", UNSET)
        connected_at: datetime.datetime | Unset
        if isinstance(_connected_at,  Unset):
            connected_at = UNSET
        else:
            connected_at = isoparse(_connected_at)




        def _parse_last_polled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_polled_at_type_0 = isoparse(data)



                return last_polled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_polled_at = _parse_last_polled_at(d.pop("lastPolledAt", UNSET))


        def _parse_import_(data: object) -> MigrationImportRun | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                import_type_1 = MigrationImportRun.from_dict(data)



                return import_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationImportRun | None | Unset, data)

        import_ = _parse_import_(d.pop("import", UNSET))


        migration_connections_item = cls(
            id=id,
            provider=provider,
            status=status,
            connected_at=connected_at,
            last_polled_at=last_polled_at,
            import_=import_,
        )


        migration_connections_item.additional_properties = d
        return migration_connections_item

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
