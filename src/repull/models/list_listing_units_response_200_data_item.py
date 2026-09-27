from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListListingUnitsResponse200DataItem")



@_attrs_define
class ListListingUnitsResponse200DataItem:
    """ 
        Attributes:
            id (str | Unset): The PMS's id for the room; `reservation.unit.id` refers to it.
            name (str | Unset):  Example: 101.
            active (bool | Unset):
            parent_id (None | str | Unset): A sub-space's parent room (a bed in a dorm), else null.
            housekeeping_status (None | str | Unset): The PMS's housekeeping state, verbatim (e.g. `Dirty`, `Clean`,
                `Inspected`).
            floor (None | str | Unset):
            source (str | Unset):  Example: mews.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    active: bool | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    housekeeping_status: None | str | Unset = UNSET
    floor: None | str | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        active = self.active

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        housekeeping_status: None | str | Unset
        if isinstance(self.housekeeping_status, Unset):
            housekeeping_status = UNSET
        else:
            housekeeping_status = self.housekeeping_status

        floor: None | str | Unset
        if isinstance(self.floor, Unset):
            floor = UNSET
        else:
            floor = self.floor

        source = self.source


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if active is not UNSET:
            field_dict["active"] = active
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if housekeeping_status is not UNSET:
            field_dict["housekeepingStatus"] = housekeeping_status
        if floor is not UNSET:
            field_dict["floor"] = floor
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        active = d.pop("active", UNSET)

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        def _parse_housekeeping_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        housekeeping_status = _parse_housekeeping_status(d.pop("housekeepingStatus", UNSET))


        def _parse_floor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor = _parse_floor(d.pop("floor", UNSET))


        source = d.pop("source", UNSET)

        list_listing_units_response_200_data_item = cls(
            id=id,
            name=name,
            active=active,
            parent_id=parent_id,
            housekeeping_status=housekeeping_status,
            floor=floor,
            source=source,
        )


        list_listing_units_response_200_data_item.additional_properties = d
        return list_listing_units_response_200_data_item

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
