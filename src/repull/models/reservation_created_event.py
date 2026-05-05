from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_created_event_type import ReservationCreatedEventType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.reservation_created_payload import ReservationCreatedPayload





T = TypeVar("T", bound="ReservationCreatedEvent")



@_attrs_define
class ReservationCreatedEvent:
    """ 
        Attributes:
            type_ (ReservationCreatedEventType):
            data (ReservationCreatedPayload): Payload for `reservation.created`. A new reservation arrived from any
                connected channel or direct booking. Stripe-pattern envelope: `data.object` carries the reservation snapshot.
            id (UUID | Unset): Stable event id — same across delivery retries of the same logical event.
            created_at (datetime.datetime | Unset):
            api_version (str | Unset):  Example: 2026-04.
     """

    type_: ReservationCreatedEventType
    data: ReservationCreatedPayload
    id: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    api_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_created_payload import ReservationCreatedPayload
        type_ = self.type_.value

        data = self.data.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        api_version = self.api_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "data": data,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_created_payload import ReservationCreatedPayload
        d = dict(src_dict)
        type_ = ReservationCreatedEventType(d.pop("type"))




        data = ReservationCreatedPayload.from_dict(d.pop("data"))




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        api_version = d.pop("apiVersion", UNSET)

        reservation_created_event = cls(
            type_=type_,
            data=data,
            id=id,
            created_at=created_at,
            api_version=api_version,
        )


        reservation_created_event.additional_properties = d
        return reservation_created_event

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
