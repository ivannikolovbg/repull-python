from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PullListingFromVrboBody")



@_attrs_define
class PullListingFromVrboBody:
    """ Optional. Omit the body to pull the listing's Vrbo listing.

        Attributes:
            vrbo_listing_number (str | Unset): The Vrbo listing number to pull, when the listing is linked to more than one
                Vrbo unit.
     """

    vrbo_listing_number: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        pull_listing_from_vrbo_body = cls(
            vrbo_listing_number=vrbo_listing_number,
        )

        return pull_listing_from_vrbo_body

