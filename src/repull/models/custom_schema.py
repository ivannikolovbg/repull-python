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





T = TypeVar("T", bound="CustomSchema")



@_attrs_define
class CustomSchema:
    """ A custom field-mapping schema owned by the workspace. Reshapes the `native` response into the workspace's preferred
    field names. Apply one per request via the `X-Schema: <name>` header on any read endpoint.

        Attributes:
            id (UUID): Stable workspace-scoped identifier.
            name (str): 3-100 lowercase chars, hyphens allowed (`^[a-z0-9][a-z0-9-]{1,98}[a-z0-9]$`). Must be unique within
                the workspace. Cannot collide with reserved names (`calry`, `calry-v1`, `native`). Example: my-app-schema.
            mappings (CustomSchemaMappings): Field-mapping table. Keys are the output field names emitted in the response
                payload; values are simple expressions referenced against the source `native` payload (dot paths, basic
                arithmetic, string concatenation). Min 1 entry, max 50 entries. Each key must be <= 100 chars; each expression
                must be <= 500 chars and pass the safety check (no `eval`, no `function`, no `process`, etc.). Example:
                {'listing_id': 'propertyId', 'arrival': 'checkIn', 'departure': 'checkOut', 'guest_name':
                "primaryGuest.firstName + ' ' + primaryGuest.lastName", 'nightly_rate': 'financials.breakdown.basePrice /
                nights'}.
            active (bool): When `false`, requests carrying this schema name in `X-Schema` fall back to `native`.
            created_at (datetime.datetime):
            description (None | str | Unset):
     """

    id: UUID
    name: str
    mappings: CustomSchemaMappings
    active: bool
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_schema_mappings import CustomSchemaMappings
        id = str(self.id)

        name = self.name

        mappings = self.mappings.to_dict()

        active = self.active

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
            "active": active,
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




        active = d.pop("active")

        created_at = isoparse(d.pop("createdAt"))




        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        custom_schema = cls(
            id=id,
            name=name,
            mappings=mappings,
            active=active,
            created_at=created_at,
            description=description,
        )


        custom_schema.additional_properties = d
        return custom_schema

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
