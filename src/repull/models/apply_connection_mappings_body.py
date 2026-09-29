from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.apply_connection_mappings_body_mappings_item import ApplyConnectionMappingsBodyMappingsItem





T = TypeVar("T", bound="ApplyConnectionMappingsBody")



@_attrs_define
class ApplyConnectionMappingsBody:
    """ 
        Attributes:
            mappings (list[ApplyConnectionMappingsBodyMappingsItem]):
            session_id (str | Unset):
     """

    mappings: list[ApplyConnectionMappingsBodyMappingsItem]
    session_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.apply_connection_mappings_body_mappings_item import ApplyConnectionMappingsBodyMappingsItem
        mappings = []
        for mappings_item_data in self.mappings:
            mappings_item = mappings_item_data.to_dict()
            mappings.append(mappings_item)



        session_id = self.session_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mappings": mappings,
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apply_connection_mappings_body_mappings_item import ApplyConnectionMappingsBodyMappingsItem
        d = dict(src_dict)
        mappings = []
        _mappings = d.pop("mappings")
        for mappings_item_data in (_mappings):
            mappings_item = ApplyConnectionMappingsBodyMappingsItem.from_dict(mappings_item_data)



            mappings.append(mappings_item)


        session_id = d.pop("sessionId", UNSET)

        apply_connection_mappings_body = cls(
            mappings=mappings,
            session_id=session_id,
        )


        apply_connection_mappings_body.additional_properties = d
        return apply_connection_mappings_body

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
