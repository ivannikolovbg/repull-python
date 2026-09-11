from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.alteration_webhook_object import AlterationWebhookObject
  from ..models.reservation_alteration_created_payload_changes import ReservationAlterationCreatedPayloadChanges





T = TypeVar("T", bound="ReservationAlterationCreatedPayload")



@_attrs_define
class ReservationAlterationCreatedPayload:
    """ Payload for `reservation.alteration.created`. A new reservation alteration was requested (Airbnb). `data.object`
    carries the snapshot; `data.changes` lists the requested field deltas.

        Attributes:
            object_ (AlterationWebhookObject): Lightweight alteration snapshot delivered as `data.object` on
                `reservation.alteration.*` events. Currently Airbnb only. Fetch full state (original vs new dates/guests/price)
                via `GET /v1/channels/airbnb/alterations` filtered by `reservation_code`.
            changes (ReservationAlterationCreatedPayloadChanges | Unset): Requested deltas keyed by field name (`checkIn`,
                `checkOut`, `guestCount`, `totalPrice`). Only changed fields appear. Example: {'checkOut': {'from':
                '2026-06-16', 'to': '2026-06-18'}, 'totalPrice': {'from': '1320.00', 'to': '1760.00'}}.
     """

    object_: AlterationWebhookObject
    changes: ReservationAlterationCreatedPayloadChanges | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.alteration_webhook_object import AlterationWebhookObject
        from ..models.reservation_alteration_created_payload_changes import ReservationAlterationCreatedPayloadChanges
        object_ = self.object_.to_dict()

        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alteration_webhook_object import AlterationWebhookObject
        from ..models.reservation_alteration_created_payload_changes import ReservationAlterationCreatedPayloadChanges
        d = dict(src_dict)
        object_ = AlterationWebhookObject.from_dict(d.pop("object"))




        _changes = d.pop("changes", UNSET)
        changes: ReservationAlterationCreatedPayloadChanges | Unset
        if isinstance(_changes,  Unset):
            changes = UNSET
        else:
            changes = ReservationAlterationCreatedPayloadChanges.from_dict(_changes)




        reservation_alteration_created_payload = cls(
            object_=object_,
            changes=changes,
        )


        reservation_alteration_created_payload.additional_properties = d
        return reservation_alteration_created_payload

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
