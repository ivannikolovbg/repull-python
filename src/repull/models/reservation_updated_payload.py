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
  from ..models.reservation_updated_payload_changes import ReservationUpdatedPayloadChanges





T = TypeVar("T", bound="ReservationUpdatedPayload")



@_attrs_define
class ReservationUpdatedPayload:
    """ Payload for `reservation.updated`. Dates, guest count, status, or pricing changed on an existing reservation. The
    `changes` map carries `{ from, to }` deltas for each field that moved.

        Attributes:
            id (int | Unset):  Example: 215906.
            confirmation_code (str | Unset):  Example: HMA1234567.
            changes (ReservationUpdatedPayloadChanges | Unset): Map of `field` → `{ from, to }` pairs describing what
                changed. Example: {'checkOut': {'from': '2026-06-05', 'to': '2026-06-07'}, 'pricing': {'from': {'total':
                '1320.00'}, 'to': {'total': '1640.00'}}}.
            updated_at (datetime.datetime | Unset):  Example: 2026-05-01T13:00:00.000Z.
     """

    id: int | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    changes: ReservationUpdatedPayloadChanges | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_updated_payload_changes import ReservationUpdatedPayloadChanges
        id = self.id

        confirmation_code = self.confirmation_code

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
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if changes is not UNSET:
            field_dict["changes"] = changes
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_updated_payload_changes import ReservationUpdatedPayloadChanges
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        confirmation_code = d.pop("confirmationCode", UNSET)

        _changes = d.pop("changes", UNSET)
        changes: ReservationUpdatedPayloadChanges | Unset
        if isinstance(_changes,  Unset):
            changes = UNSET
        else:
            changes = ReservationUpdatedPayloadChanges.from_dict(_changes)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        reservation_updated_payload = cls(
            id=id,
            confirmation_code=confirmation_code,
            changes=changes,
            updated_at=updated_at,
        )


        reservation_updated_payload.additional_properties = d
        return reservation_updated_payload

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
