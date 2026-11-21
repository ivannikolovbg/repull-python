from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.vrbo_listing_action_response_200_units_item import VrboListingActionResponse200UnitsItem





T = TypeVar("T", bound="VrboListingActionResponse200")



@_attrs_define
class VrboListingActionResponse200:
    """ 
        Attributes:
            id (str | Unset):
            action (str | Unset):
            channel (str | Unset):  Example: vrbo.
            live (bool | Unset): What Vrbo now shows (read back).
            active (bool | Unset): `delete`: the Repull record.
            units (list[VrboListingActionResponse200UnitsItem] | Unset):
     """

    id: str | Unset = UNSET
    action: str | Unset = UNSET
    channel: str | Unset = UNSET
    live: bool | Unset = UNSET
    active: bool | Unset = UNSET
    units: list[VrboListingActionResponse200UnitsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vrbo_listing_action_response_200_units_item import VrboListingActionResponse200UnitsItem
        id = self.id

        action = self.action

        channel = self.channel

        live = self.live

        active = self.active

        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if action is not UNSET:
            field_dict["action"] = action
        if channel is not UNSET:
            field_dict["channel"] = channel
        if live is not UNSET:
            field_dict["live"] = live
        if active is not UNSET:
            field_dict["active"] = active
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vrbo_listing_action_response_200_units_item import VrboListingActionResponse200UnitsItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        action = d.pop("action", UNSET)

        channel = d.pop("channel", UNSET)

        live = d.pop("live", UNSET)

        active = d.pop("active", UNSET)

        _units = d.pop("units", UNSET)
        units: list[VrboListingActionResponse200UnitsItem] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = VrboListingActionResponse200UnitsItem.from_dict(units_item_data)



                units.append(units_item)


        vrbo_listing_action_response_200 = cls(
            id=id,
            action=action,
            channel=channel,
            live=live,
            active=active,
            units=units,
        )


        vrbo_listing_action_response_200.additional_properties = d
        return vrbo_listing_action_response_200

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
