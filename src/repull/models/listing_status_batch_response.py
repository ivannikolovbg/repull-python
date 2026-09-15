from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListingStatusBatchResponse")



@_attrs_define
class ListingStatusBatchResponse:
    """ 
        Attributes:
            active (bool): The state every listing in the request is now in.
            updated (list[str]): Listing ids whose state this call changed, in request order.
            unchanged (list[str]): Listing ids that were already in the requested state, in request order.
     """

    active: bool
    updated: list[str]
    unchanged: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        active = self.active

        updated = self.updated



        unchanged = self.unchanged




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "active": active,
            "updated": updated,
            "unchanged": unchanged,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        updated = cast(list[str], d.pop("updated"))


        unchanged = cast(list[str], d.pop("unchanged"))


        listing_status_batch_response = cls(
            active=active,
            updated=updated,
            unchanged=unchanged,
        )


        listing_status_batch_response.additional_properties = d
        return listing_status_batch_response

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
