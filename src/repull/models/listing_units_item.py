from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingUnitsItem")



@_attrs_define
class ListingUnitsItem:
    """ 
        Attributes:
            id (str | Unset): Unit id — what `reservation.unit.id` and the per-night `units[].id` on availability refer to.
            name (str | Unset):
            active (bool | Unset):
            parent_id (None | str | Unset):
            housekeeping_status (None | str | Unset):
            floor (None | str | Unset):
            source (str | Unset): The PMS the unit comes from: `cloudbeds`, `mews`, `guesty`, …
            listing_id (None | str | Unset): The unit's own Repull listing id when the unit is a listing too (a Guesty
                multi-unit listing's units, each with its own calendar), else `null`.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    active: bool | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    housekeeping_status: None | str | Unset = UNSET
    floor: None | str | Unset = UNSET
    source: str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
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

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id


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
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id

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

        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        listing_units_item = cls(
            id=id,
            name=name,
            active=active,
            parent_id=parent_id,
            housekeeping_status=housekeeping_status,
            floor=floor,
            source=source,
            listing_id=listing_id,
        )


        listing_units_item.additional_properties = d
        return listing_units_item

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
