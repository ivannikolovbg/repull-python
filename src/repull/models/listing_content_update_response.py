from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateResponse")



@_attrs_define
class ListingContentUpdateResponse:
    """ 
        Attributes:
            id (str | Unset): The listing id (serialized as a string to preserve precision).
            changed (list[str] | Unset): Content slabs that were actually written, e.g. ["title","occupancy","amenities"].
            deferred (list[str] | Unset): Provided-but-not-applied fields — e.g. "photos" when a non-empty photos array
                carried no valid http(s) URL.
     """

    id: str | Unset = UNSET
    changed: list[str] | Unset = UNSET
    deferred: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        changed: list[str] | Unset = UNSET
        if not isinstance(self.changed, Unset):
            changed = self.changed



        deferred: list[str] | Unset = UNSET
        if not isinstance(self.deferred, Unset):
            deferred = self.deferred




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if changed is not UNSET:
            field_dict["changed"] = changed
        if deferred is not UNSET:
            field_dict["deferred"] = deferred

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        changed = cast(list[str], d.pop("changed", UNSET))


        deferred = cast(list[str], d.pop("deferred", UNSET))


        listing_content_update_response = cls(
            id=id,
            changed=changed,
            deferred=deferred,
        )


        listing_content_update_response.additional_properties = d
        return listing_content_update_response

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
