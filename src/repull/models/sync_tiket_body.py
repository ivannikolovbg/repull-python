from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SyncTiketBody")



@_attrs_define
class SyncTiketBody:
    """ 
        Attributes:
            property_id (str | Unset): tiket.com Hotel ID. Omit for every active property.
            refresh_products (bool | Unset): Re-read room types and rate plans first. Default: False.
     """

    property_id: str | Unset = UNSET
    refresh_products: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id

        refresh_products = self.refresh_products


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["property_id"] = property_id
        if refresh_products is not UNSET:
            field_dict["refresh_products"] = refresh_products

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_id = d.pop("property_id", UNSET)

        refresh_products = d.pop("refresh_products", UNSET)

        sync_tiket_body = cls(
            property_id=property_id,
            refresh_products=refresh_products,
        )


        sync_tiket_body.additional_properties = d
        return sync_tiket_body

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
