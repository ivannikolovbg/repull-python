from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateVrboListingLocationBody")



@_attrs_define
class UpdateVrboListingLocationBody:
    """ 
        Attributes:
            show_exact_location (bool):
     """

    show_exact_location: bool





    def to_dict(self) -> dict[str, Any]:
        show_exact_location = self.show_exact_location


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "showExactLocation": show_exact_location,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        show_exact_location = d.pop("showExactLocation")

        update_vrbo_listing_location_body = cls(
            show_exact_location=show_exact_location,
        )

        return update_vrbo_listing_location_body

