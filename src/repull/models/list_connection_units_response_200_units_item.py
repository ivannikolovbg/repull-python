from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_connection_units_response_200_units_item_meta import ListConnectionUnitsResponse200UnitsItemMeta





T = TypeVar("T", bound="ListConnectionUnitsResponse200UnitsItem")



@_attrs_define
class ListConnectionUnitsResponse200UnitsItem:
    """ 
        Attributes:
            unit_id (str | Unset):
            unit_name (str | Unset):
            grain (str | Unset):
            current_listing_id (int | None | Unset):
            suggested_listing_id (int | None | Unset):
            meta (ListConnectionUnitsResponse200UnitsItemMeta | Unset):
     """

    unit_id: str | Unset = UNSET
    unit_name: str | Unset = UNSET
    grain: str | Unset = UNSET
    current_listing_id: int | None | Unset = UNSET
    suggested_listing_id: int | None | Unset = UNSET
    meta: ListConnectionUnitsResponse200UnitsItemMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_connection_units_response_200_units_item_meta import ListConnectionUnitsResponse200UnitsItemMeta
        unit_id = self.unit_id

        unit_name = self.unit_name

        grain = self.grain

        current_listing_id: int | None | Unset
        if isinstance(self.current_listing_id, Unset):
            current_listing_id = UNSET
        else:
            current_listing_id = self.current_listing_id

        suggested_listing_id: int | None | Unset
        if isinstance(self.suggested_listing_id, Unset):
            suggested_listing_id = UNSET
        else:
            suggested_listing_id = self.suggested_listing_id

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if unit_id is not UNSET:
            field_dict["unit_id"] = unit_id
        if unit_name is not UNSET:
            field_dict["unit_name"] = unit_name
        if grain is not UNSET:
            field_dict["grain"] = grain
        if current_listing_id is not UNSET:
            field_dict["current_listing_id"] = current_listing_id
        if suggested_listing_id is not UNSET:
            field_dict["suggested_listing_id"] = suggested_listing_id
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_connection_units_response_200_units_item_meta import ListConnectionUnitsResponse200UnitsItemMeta
        d = dict(src_dict)
        unit_id = d.pop("unit_id", UNSET)

        unit_name = d.pop("unit_name", UNSET)

        grain = d.pop("grain", UNSET)

        def _parse_current_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_listing_id = _parse_current_listing_id(d.pop("current_listing_id", UNSET))


        def _parse_suggested_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        suggested_listing_id = _parse_suggested_listing_id(d.pop("suggested_listing_id", UNSET))


        _meta = d.pop("meta", UNSET)
        meta: ListConnectionUnitsResponse200UnitsItemMeta | Unset
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = ListConnectionUnitsResponse200UnitsItemMeta.from_dict(_meta)




        list_connection_units_response_200_units_item = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            grain=grain,
            current_listing_id=current_listing_id,
            suggested_listing_id=suggested_listing_id,
            meta=meta,
        )


        list_connection_units_response_200_units_item.additional_properties = d
        return list_connection_units_response_200_units_item

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
