from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreatePriceLabsKeyBody")



@_attrs_define
class CreatePriceLabsKeyBody:
    """ 
        Attributes:
            listing_ids (list[str] | Unset): Only these listings of the workspace (`GET /v1/properties`). Omit for every
                listing, new ones included. Example: ['4118', '4119'].
            label (str | Unset): A name for the connection. Example: PriceLabs — beach houses.
     """

    listing_ids: list[str] | Unset = UNSET
    label: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        listing_ids: list[str] | Unset = UNSET
        if not isinstance(self.listing_ids, Unset):
            listing_ids = self.listing_ids



        label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if listing_ids is not UNSET:
            field_dict["listingIds"] = listing_ids
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_ids = cast(list[str], d.pop("listingIds", UNSET))


        label = d.pop("label", UNSET)

        create_price_labs_key_body = cls(
            listing_ids=listing_ids,
            label=label,
        )

        return create_price_labs_key_body

