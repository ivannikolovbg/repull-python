from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.custom_schema_mappings import CustomSchemaMappings





T = TypeVar("T", bound="CustomSchemaCreateResponse")



@_attrs_define
class CustomSchemaCreateResponse:
    """ Returned by `POST /v1/schema/custom` (201). Includes a `usage` hint telling the caller exactly which header value to
    set on subsequent requests.

        Attributes:
            id (UUID):
            name (str):
            mappings (CustomSchemaMappings): Field-mapping table. Keys are the output field names emitted in the response
                payload; values are simple expressions referenced against the source `native` payload (dot paths, basic
                arithmetic, string concatenation). Min 1 entry, max 50 entries. Each key must be <= 100 chars; each expression
                must be <= 500 chars and pass the safety check (no `eval`, no `function`, no `process`, etc.). Example:
                {'listing_id': 'propertyId', 'arrival': 'checkIn', 'departure': 'checkOut', 'guest_name':
                "primaryGuest.firstName + ' ' + primaryGuest.lastName", 'nightly_rate': 'financials.breakdown.basePrice /
                nights'}.
            usage (str):  Example: Set header: X-Schema: my-app-schema.
            created_at (datetime.datetime):
            description (None | str | Unset):
     """

    id: UUID
    name: str
    mappings: CustomSchemaMappings
    usage: str
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_schema_mappings import CustomSchemaMappings
        id = str(self.id)

        name = self.name

        mappings = self.mappings.to_dict()

        usage = self.usage

        created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "mappings": mappings,
            "usage": usage,
            "createdAt": created_at,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_schema_mappings import CustomSchemaMappings
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        mappings = CustomSchemaMappings.from_dict(d.pop("mappings"))




        usage = d.pop("usage")

        created_at = isoparse(d.pop("createdAt"))




        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        custom_schema_create_response = cls(
            id=id,
            name=name,
            mappings=mappings,
            usage=usage,
            created_at=created_at,
            description=description,
        )


        custom_schema_create_response.additional_properties = d
        return custom_schema_create_response

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
