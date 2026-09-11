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
  from ..models.alteration_webhook_object import AlterationWebhookObject





T = TypeVar("T", bound="ReservationAlterationRespondedPayload")



@_attrs_define
class ReservationAlterationRespondedPayload:
    """ Payload for `reservation.alteration.responded`. A pending alteration was accepted, declined, or cancelled.
    `data.object.status` reflects the new state.

        Attributes:
            object_ (AlterationWebhookObject): Lightweight alteration snapshot delivered as `data.object` on
                `reservation.alteration.*` events. Currently Airbnb only. Fetch full state (original vs new dates/guests/price)
                via `GET /v1/channels/airbnb/alterations` filtered by `reservation_code`.
            responded_at (datetime.datetime | Unset): When the response was recorded. Example: 2026-05-01T16:30:00.000Z.
     """

    object_: AlterationWebhookObject
    responded_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.alteration_webhook_object import AlterationWebhookObject
        object_ = self.object_.to_dict()

        responded_at: str | Unset = UNSET
        if not isinstance(self.responded_at, Unset):
            responded_at = self.responded_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if responded_at is not UNSET:
            field_dict["respondedAt"] = responded_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alteration_webhook_object import AlterationWebhookObject
        d = dict(src_dict)
        object_ = AlterationWebhookObject.from_dict(d.pop("object"))




        _responded_at = d.pop("respondedAt", UNSET)
        responded_at: datetime.datetime | Unset
        if isinstance(_responded_at,  Unset):
            responded_at = UNSET
        else:
            responded_at = isoparse(_responded_at)




        reservation_alteration_responded_payload = cls(
            object_=object_,
            responded_at=responded_at,
        )


        reservation_alteration_responded_payload.additional_properties = d
        return reservation_alteration_responded_payload

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
