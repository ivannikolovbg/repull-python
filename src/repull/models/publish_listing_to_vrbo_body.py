from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PublishListingToVrboBody")



@_attrs_define
class PublishListingToVrboBody:
    """ 
        Attributes:
            account_id (str | Unset): The Vrbo account, as its connection id (`"vrbo:13"`) or the bare number. Needed only
                when the workspace has several.
            property_id (str | Unset): Finish this unpublished Vrbo property (from a failed run's `job.propertyId`) instead
                of starting a new one.
     """

    account_id: str | Unset = UNSET
    property_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        property_id = self.property_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        property_id = d.pop("propertyId", UNSET)

        publish_listing_to_vrbo_body = cls(
            account_id=account_id,
            property_id=property_id,
        )

        return publish_listing_to_vrbo_body

