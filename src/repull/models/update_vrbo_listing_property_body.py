from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_property_body_interior_size import UpdateVrboListingPropertyBodyInteriorSize





T = TypeVar("T", bound="UpdateVrboListingPropertyBody")



@_attrs_define
class UpdateVrboListingPropertyBody:
    """ 
        Attributes:
            property_type (str | Unset): One of the read's `propertyTypeOptions[].value`.
            property_name (str | Unset): Internal name (not shown to guests).
            interior_size (UpdateVrboListingPropertyBodyInteriorSize | Unset):
            seniors_only (bool | Unset):
            long_term_renters_welcome (bool | Unset):
     """

    property_type: str | Unset = UNSET
    property_name: str | Unset = UNSET
    interior_size: UpdateVrboListingPropertyBodyInteriorSize | Unset = UNSET
    seniors_only: bool | Unset = UNSET
    long_term_renters_welcome: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_property_body_interior_size import UpdateVrboListingPropertyBodyInteriorSize
        property_type = self.property_type

        property_name = self.property_name

        interior_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interior_size, Unset):
            interior_size = self.interior_size.to_dict()

        seniors_only = self.seniors_only

        long_term_renters_welcome = self.long_term_renters_welcome


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if property_name is not UNSET:
            field_dict["propertyName"] = property_name
        if interior_size is not UNSET:
            field_dict["interiorSize"] = interior_size
        if seniors_only is not UNSET:
            field_dict["seniorsOnly"] = seniors_only
        if long_term_renters_welcome is not UNSET:
            field_dict["longTermRentersWelcome"] = long_term_renters_welcome

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_property_body_interior_size import UpdateVrboListingPropertyBodyInteriorSize
        d = dict(src_dict)
        property_type = d.pop("propertyType", UNSET)

        property_name = d.pop("propertyName", UNSET)

        _interior_size = d.pop("interiorSize", UNSET)
        interior_size: UpdateVrboListingPropertyBodyInteriorSize | Unset
        if isinstance(_interior_size,  Unset):
            interior_size = UNSET
        else:
            interior_size = UpdateVrboListingPropertyBodyInteriorSize.from_dict(_interior_size)




        seniors_only = d.pop("seniorsOnly", UNSET)

        long_term_renters_welcome = d.pop("longTermRentersWelcome", UNSET)

        update_vrbo_listing_property_body = cls(
            property_type=property_type,
            property_name=property_name,
            interior_size=interior_size,
            seniors_only=seniors_only,
            long_term_renters_welcome=long_term_renters_welcome,
        )

        return update_vrbo_listing_property_body

