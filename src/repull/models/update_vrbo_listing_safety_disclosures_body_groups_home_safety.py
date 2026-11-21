from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_safety_disclosures_body_groups_home_safety_values import UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafetyValues





T = TypeVar("T", bound="UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety")



@_attrs_define
class UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafety:
    """ 
        Attributes:
            values (UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafetyValues):
     """

    values: UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafetyValues





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_safety_disclosures_body_groups_home_safety_values import UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafetyValues
        values = self.values.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "values": values,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_safety_disclosures_body_groups_home_safety_values import UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafetyValues
        d = dict(src_dict)
        values = UpdateVrboListingSafetyDisclosuresBodyGroupsHomeSafetyValues.from_dict(d.pop("values"))




        update_vrbo_listing_safety_disclosures_body_groups_home_safety = cls(
            values=values,
        )

        return update_vrbo_listing_safety_disclosures_body_groups_home_safety

