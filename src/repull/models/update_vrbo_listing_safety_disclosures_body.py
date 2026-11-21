from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_safety_disclosures_body_groups import UpdateVrboListingSafetyDisclosuresBodyGroups





T = TypeVar("T", bound="UpdateVrboListingSafetyDisclosuresBody")



@_attrs_define
class UpdateVrboListingSafetyDisclosuresBody:
    """ 
        Attributes:
            groups (UpdateVrboListingSafetyDisclosuresBodyGroups):
     """

    groups: UpdateVrboListingSafetyDisclosuresBodyGroups





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_safety_disclosures_body_groups import UpdateVrboListingSafetyDisclosuresBodyGroups
        groups = self.groups.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "groups": groups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_safety_disclosures_body_groups import UpdateVrboListingSafetyDisclosuresBodyGroups
        d = dict(src_dict)
        groups = UpdateVrboListingSafetyDisclosuresBodyGroups.from_dict(d.pop("groups"))




        update_vrbo_listing_safety_disclosures_body = cls(
            groups=groups,
        )

        return update_vrbo_listing_safety_disclosures_body

