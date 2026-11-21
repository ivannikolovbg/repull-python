from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_amenities_body_groups_entertainment_values import UpdateVrboListingAmenitiesBodyGroupsEntertainmentValues





T = TypeVar("T", bound="UpdateVrboListingAmenitiesBodyGroupsEntertainment")



@_attrs_define
class UpdateVrboListingAmenitiesBodyGroupsEntertainment:
    """ 
        Attributes:
            values (UpdateVrboListingAmenitiesBodyGroupsEntertainmentValues): `{fieldId: value}`
     """

    values: UpdateVrboListingAmenitiesBodyGroupsEntertainmentValues





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_amenities_body_groups_entertainment_values import UpdateVrboListingAmenitiesBodyGroupsEntertainmentValues
        values = self.values.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "values": values,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_amenities_body_groups_entertainment_values import UpdateVrboListingAmenitiesBodyGroupsEntertainmentValues
        d = dict(src_dict)
        values = UpdateVrboListingAmenitiesBodyGroupsEntertainmentValues.from_dict(d.pop("values"))




        update_vrbo_listing_amenities_body_groups_entertainment = cls(
            values=values,
        )

        return update_vrbo_listing_amenities_body_groups_entertainment

