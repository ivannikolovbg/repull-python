from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_safety_disclosures_body_groups_home_safety import UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety
  from ..models.update_vrbo_listing_safety_disclosures_body_groups_safety_devices import UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices





T = TypeVar("T", bound="UpdateVrboListingSafetyDisclosuresBodyGroups")



@_attrs_define
class UpdateVrboListingSafetyDisclosuresBodyGroups:
    """ 
        Attributes:
            home_safety (UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety | Unset):
            safety_devices (UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices | Unset):
     """

    home_safety: UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety | Unset = UNSET
    safety_devices: UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_safety_disclosures_body_groups_home_safety import UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety
        from ..models.update_vrbo_listing_safety_disclosures_body_groups_safety_devices import UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices
        home_safety: dict[str, Any] | Unset = UNSET
        if not isinstance(self.home_safety, Unset):
            home_safety = self.home_safety.to_dict()

        safety_devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.safety_devices, Unset):
            safety_devices = self.safety_devices.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if home_safety is not UNSET:
            field_dict["homeSafety"] = home_safety
        if safety_devices is not UNSET:
            field_dict["safetyDevices"] = safety_devices

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_safety_disclosures_body_groups_home_safety import UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety
        from ..models.update_vrbo_listing_safety_disclosures_body_groups_safety_devices import UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices
        d = dict(src_dict)
        _home_safety = d.pop("homeSafety", UNSET)
        home_safety: UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety | Unset
        if isinstance(_home_safety,  Unset):
            home_safety = UNSET
        else:
            home_safety = UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety.from_dict(_home_safety)




        _safety_devices = d.pop("safetyDevices", UNSET)
        safety_devices: UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices | Unset
        if isinstance(_safety_devices,  Unset):
            safety_devices = UNSET
        else:
            safety_devices = UpdateVrboListingSafetyDisclosuresBodyGroupsSafetyDevices.from_dict(_safety_devices)




        update_vrbo_listing_safety_disclosures_body_groups = cls(
            home_safety=home_safety,
            safety_devices=safety_devices,
        )

        return update_vrbo_listing_safety_disclosures_body_groups

