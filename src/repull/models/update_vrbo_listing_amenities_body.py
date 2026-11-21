from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_amenities_body_groups import UpdateVrboListingAmenitiesBodyGroups





T = TypeVar("T", bound="UpdateVrboListingAmenitiesBody")



@_attrs_define
class UpdateVrboListingAmenitiesBody:
    """ 
        Attributes:
            groups (UpdateVrboListingAmenitiesBodyGroups): Keyed by group: essentials, internet, climateControl, general,
                office, kitchenAndDining, parking, poolAndSpa, sustainability, entertainment, outdoor, onsiteService,
                accessibility, homeSafety, safetyDevices, enhancedCleaning, locationAndView, localAttractionsAndActivities,
                checkoutInstructions.
     """

    groups: UpdateVrboListingAmenitiesBodyGroups





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_amenities_body_groups import UpdateVrboListingAmenitiesBodyGroups
        groups = self.groups.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "groups": groups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_amenities_body_groups import UpdateVrboListingAmenitiesBodyGroups
        d = dict(src_dict)
        groups = UpdateVrboListingAmenitiesBodyGroups.from_dict(d.pop("groups"))




        update_vrbo_listing_amenities_body = cls(
            groups=groups,
        )

        return update_vrbo_listing_amenities_body

