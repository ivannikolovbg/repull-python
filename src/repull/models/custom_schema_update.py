from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_schema_mappings import CustomSchemaMappings





T = TypeVar("T", bound="CustomSchemaUpdate")



@_attrs_define
class CustomSchemaUpdate:
    """ Request body for `PATCH /v1/schema/custom/{id}`. All fields optional; omitted fields are left unchanged. `name` is
    intentionally NOT patchable — create a new schema and migrate consumers if you need to rename.

        Attributes:
            description (None | str | Unset):
            mappings (CustomSchemaMappings | Unset): Field-mapping table. Keys are the output field names emitted in the
                response payload; values are simple expressions referenced against the source `native` payload (dot paths, basic
                arithmetic, string concatenation). Min 1 entry, max 50 entries. Each key must be <= 100 chars; each expression
                must be <= 500 chars and pass the safety check (no `eval`, no `function`, no `process`, etc.). Example:
                {'listing_id': 'propertyId', 'arrival': 'checkIn', 'departure': 'checkOut', 'guest_name':
                "primaryGuest.firstName + ' ' + primaryGuest.lastName", 'nightly_rate': 'financials.breakdown.basePrice /
                nights'}.
            active (bool | Unset): Toggle the schema on/off. When `false`, requests carrying this schema name in `X-Schema`
                fall back to `native`.
     """

    description: None | str | Unset = UNSET
    mappings: CustomSchemaMappings | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_schema_mappings import CustomSchemaMappings
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mappings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = self.mappings.to_dict()

        active = self.active


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if mappings is not UNSET:
            field_dict["mappings"] = mappings
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_schema_mappings import CustomSchemaMappings
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _mappings = d.pop("mappings", UNSET)
        mappings: CustomSchemaMappings | Unset
        if isinstance(_mappings,  Unset):
            mappings = UNSET
        else:
            mappings = CustomSchemaMappings.from_dict(_mappings)




        active = d.pop("active", UNSET)

        custom_schema_update = cls(
            description=description,
            mappings=mappings,
            active=active,
        )


        custom_schema_update.additional_properties = d
        return custom_schema_update

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
