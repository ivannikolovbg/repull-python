from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ApplyConnectionMappingsBodyMappingsItem")



@_attrs_define
class ApplyConnectionMappingsBodyMappingsItem:
    """ 
        Attributes:
            unit_id (str):
            listing_id (int | None | Unset):
            create (bool | Unset):
            calendar_sync (bool | Unset): Vrbo: push this listing's prices and availability to Vrbo. Omit to follow the
                connection's access type (`messaging` = off, `full_access` = on). A new listing (`create`) always follows the
                access type. Other channels ignore it.
     """

    unit_id: str
    listing_id: int | None | Unset = UNSET
    create: bool | Unset = UNSET
    calendar_sync: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        unit_id = self.unit_id

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        create = self.create

        calendar_sync = self.calendar_sync


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "unitId": unit_id,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if create is not UNSET:
            field_dict["create"] = create
        if calendar_sync is not UNSET:
            field_dict["calendarSync"] = calendar_sync

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_id = d.pop("unitId")

        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        create = d.pop("create", UNSET)

        calendar_sync = d.pop("calendarSync", UNSET)

        apply_connection_mappings_body_mappings_item = cls(
            unit_id=unit_id,
            listing_id=listing_id,
            create=create,
            calendar_sync=calendar_sync,
        )


        apply_connection_mappings_body_mappings_item.additional_properties = d
        return apply_connection_mappings_body_mappings_item

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
