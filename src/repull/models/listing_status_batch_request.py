from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListingStatusBatchRequest")



@_attrs_define
class ListingStatusBatchRequest:
    """ 
        Attributes:
            listing_ids (list[str]): Listing ids to change, 1 to 500, each at most once. Send them as returned by `GET
                /v1/listings` (strings); plain integers are accepted too.
            active (bool): `false` deactivates every listing in `listingIds`; `true` activates them. Active listings count
                toward your plan's listing limit.
     """

    listing_ids: list[str]
    active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_ids = self.listing_ids



        active = self.active


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingIds": listing_ids,
            "active": active,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_ids = cast(list[str], d.pop("listingIds"))


        active = d.pop("active")

        listing_status_batch_request = cls(
            listing_ids=listing_ids,
            active=active,
        )


        listing_status_batch_request.additional_properties = d
        return listing_status_batch_request

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
