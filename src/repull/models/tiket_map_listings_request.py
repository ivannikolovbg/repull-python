from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_map_listings_request_mappings_item import TiketMapListingsRequestMappingsItem





T = TypeVar("T", bound="TiketMapListingsRequest")



@_attrs_define
class TiketMapListingsRequest:
    """ 
        Attributes:
            property_id (str): tiket.com Hotel ID.
            mappings (list[TiketMapListingsRequestMappingsItem]):
     """

    property_id: str
    mappings: list[TiketMapListingsRequestMappingsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_map_listings_request_mappings_item import TiketMapListingsRequestMappingsItem
        property_id = self.property_id

        mappings = []
        for mappings_item_data in self.mappings:
            mappings_item = mappings_item_data.to_dict()
            mappings.append(mappings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "property_id": property_id,
            "mappings": mappings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_map_listings_request_mappings_item import TiketMapListingsRequestMappingsItem
        d = dict(src_dict)
        property_id = d.pop("property_id")

        mappings = []
        _mappings = d.pop("mappings")
        for mappings_item_data in (_mappings):
            mappings_item = TiketMapListingsRequestMappingsItem.from_dict(mappings_item_data)



            mappings.append(mappings_item)


        tiket_map_listings_request = cls(
            property_id=property_id,
            mappings=mappings,
        )


        tiket_map_listings_request.additional_properties = d
        return tiket_map_listings_request

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
