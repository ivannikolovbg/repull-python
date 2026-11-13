from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.start_connection_import_response_202_data_scope import StartConnectionImportResponse202DataScope
from ..models.start_connection_import_response_202_data_status import StartConnectionImportResponse202DataStatus
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="StartConnectionImportResponse202Data")



@_attrs_define
class StartConnectionImportResponse202Data:
    """ 
        Attributes:
            connection (str): The connection handle, e.g. `airbnb:1234567`.
            scope (StartConnectionImportResponse202DataScope):
            status (StartConnectionImportResponse202DataStatus):
            queued_at (datetime.datetime):
     """

    connection: str
    scope: StartConnectionImportResponse202DataScope
    status: StartConnectionImportResponse202DataStatus
    queued_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        connection = self.connection

        scope = self.scope.value

        status = self.status.value

        queued_at = self.queued_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connection": connection,
            "scope": scope,
            "status": status,
            "queuedAt": queued_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection = d.pop("connection")

        scope = StartConnectionImportResponse202DataScope(d.pop("scope"))




        status = StartConnectionImportResponse202DataStatus(d.pop("status"))




        queued_at = isoparse(d.pop("queuedAt"))




        start_connection_import_response_202_data = cls(
            connection=connection,
            scope=scope,
            status=status,
            queued_at=queued_at,
        )


        start_connection_import_response_202_data.additional_properties = d
        return start_connection_import_response_202_data

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
