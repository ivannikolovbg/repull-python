from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_cancelled_event_type import ReservationCancelledEventType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.reservation_cancelled_payload import ReservationCancelledPayload





T = TypeVar("T", bound="ReservationCancelledEvent")



@_attrs_define
class ReservationCancelledEvent:
    """ 
        Attributes:
            type_ (ReservationCancelledEventType):
            data (ReservationCancelledPayload): Payload for `reservation.cancelled`. A reservation was cancelled by the
                guest, host, or platform.
            id (UUID | Unset):
            created_at (datetime.datetime | Unset):
            api_version (str | Unset):
     """

    type_: ReservationCancelledEventType
    data: ReservationCancelledPayload
    id: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    api_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_cancelled_payload import ReservationCancelledPayload
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
        from ..models.reservation_cancelled_payload import ReservationCancelledPayload
        d = dict(src_dict)
        type_ = ReservationCancelledEventType(d.pop("type"))




        data = ReservationCancelledPayload.from_dict(d.pop("data"))




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

        reservation_cancelled_event = cls(
            type_=type_,
            data=data,
            id=id,
            created_at=created_at,
            api_version=api_version,
        )


        reservation_cancelled_event.additional_properties = d
        return reservation_cancelled_event

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
