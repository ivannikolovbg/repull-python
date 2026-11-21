from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MapVrboListingResponse200")



@_attrs_define
class MapVrboListingResponse200:
    """ 
        Attributes:
            success (bool | Unset):
            vrbo_listing_number (str | Unset):
            listing_id (str | Unset):
            created (bool | Unset):
            account_id (str | Unset):
     """

    success: bool | Unset = UNSET
    vrbo_listing_number: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    created: bool | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        vrbo_listing_number = self.vrbo_listing_number

        listing_id = self.listing_id

        created = self.created

        account_id = self.account_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success is not UNSET:
            field_dict["success"] = success
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if created is not UNSET:
            field_dict["created"] = created
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        listing_id = d.pop("listingId", UNSET)

        created = d.pop("created", UNSET)

        account_id = d.pop("accountId", UNSET)

        map_vrbo_listing_response_200 = cls(
            success=success,
            vrbo_listing_number=vrbo_listing_number,
            listing_id=listing_id,
            created=created,
            account_id=account_id,
        )


        map_vrbo_listing_response_200.additional_properties = d
        return map_vrbo_listing_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
