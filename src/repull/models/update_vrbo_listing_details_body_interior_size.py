from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_details_body_interior_size_unit import UpdateVrboListingDetailsBodyInteriorSizeUnit






T = TypeVar("T", bound="UpdateVrboListingDetailsBodyInteriorSize")



@_attrs_define
class UpdateVrboListingDetailsBodyInteriorSize:
    """ 
        Attributes:
            value (float):
            unit (UpdateVrboListingDetailsBodyInteriorSizeUnit):
     """

    value: float
    unit: UpdateVrboListingDetailsBodyInteriorSizeUnit





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit = self.unit.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
            "unit": unit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        unit = UpdateVrboListingDetailsBodyInteriorSizeUnit(d.pop("unit"))




        update_vrbo_listing_details_body_interior_size = cls(
            value=value,
            unit=unit,
        )

        return update_vrbo_listing_details_body_interior_size

