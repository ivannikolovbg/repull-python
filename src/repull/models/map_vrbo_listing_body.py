from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MapVrboListingBody")



@_attrs_define
class MapVrboListingBody:
    """ 
        Attributes:
            vrbo_listing_number (str): The number in the Vrbo URL (vrbo.com/5506023). Example: 5506023.
            listing_id (int | Unset): The Repull listing to link it to. Or `create: true`. Example: 6199.
            create (bool | Unset): Create a Repull listing from what Vrbo shows, instead of `listingId`.
            account_id (str | Unset): The Vrbo account the unit is on, when the workspace has several. Example:
                vrbo:7001234.
            sync_enabled (bool | Unset): Also send the listing's calendar to Vrbo.
     """

    vrbo_listing_number: str
    listing_id: int | Unset = UNSET
    create: bool | Unset = UNSET
    account_id: str | Unset = UNSET
    sync_enabled: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        vrbo_listing_number = self.vrbo_listing_number

        listing_id = self.listing_id

        create = self.create

        account_id = self.account_id

        sync_enabled = self.sync_enabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "vrboListingNumber": vrbo_listing_number,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if create is not UNSET:
            field_dict["create"] = create
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vrbo_listing_number = d.pop("vrboListingNumber")

        listing_id = d.pop("listingId", UNSET)

        create = d.pop("create", UNSET)

        account_id = d.pop("accountId", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        map_vrbo_listing_body = cls(
            vrbo_listing_number=vrbo_listing_number,
            listing_id=listing_id,
            create=create,
            account_id=account_id,
            sync_enabled=sync_enabled,
        )

        return map_vrbo_listing_body

