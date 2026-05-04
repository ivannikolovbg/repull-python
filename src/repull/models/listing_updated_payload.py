from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_updated_payload_changes import ListingUpdatedPayloadChanges





T = TypeVar("T", bound="ListingUpdatedPayload")



@_attrs_define
class ListingUpdatedPayload:
    """ Payload for `listing.updated`. Listing content, amenities, photos, or status changed.

        Attributes:
            id (int | Unset):  Example: 6250.
            changes (ListingUpdatedPayloadChanges | Unset): Map of `field` → `{ from, to }` pairs describing what changed.
                Example: {'title': {'from': 'R-Sable 1302', 'to': 'R-Sable 1302 — Radium Hot Springs'}}.
            updated_at (datetime.datetime | Unset):  Example: 2026-05-01T12:30:00.000Z.
     """

    id: int | Unset = UNSET
    changes: ListingUpdatedPayloadChanges | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_updated_payload_changes import ListingUpdatedPayloadChanges
        id = self.id

        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if changes is not UNSET:
            field_dict["changes"] = changes
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_updated_payload_changes import ListingUpdatedPayloadChanges
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _changes = d.pop("changes", UNSET)
        changes: ListingUpdatedPayloadChanges | Unset
        if isinstance(_changes,  Unset):
            changes = UNSET
        else:
            changes = ListingUpdatedPayloadChanges.from_dict(_changes)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        listing_updated_payload = cls(
            id=id,
            changes=changes,
            updated_at=updated_at,
        )


        listing_updated_payload.additional_properties = d
        return listing_updated_payload

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
