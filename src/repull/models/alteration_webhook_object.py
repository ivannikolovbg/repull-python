from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.alteration_webhook_object_initiator_type_1 import AlterationWebhookObjectInitiatorType1
from ..models.alteration_webhook_object_initiator_type_2_type_1 import AlterationWebhookObjectInitiatorType2Type1
from ..models.alteration_webhook_object_initiator_type_3_type_1 import AlterationWebhookObjectInitiatorType3Type1
from ..models.alteration_webhook_object_status import AlterationWebhookObjectStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AlterationWebhookObject")



@_attrs_define
class AlterationWebhookObject:
    """ Lightweight alteration snapshot delivered as `data.object` on `reservation.alteration.*` events. Currently Airbnb
    only. Fetch full state (original vs new dates/guests/price) via `GET /v1/channels/airbnb/alterations` filtered by
    `reservation_code`.

        Attributes:
            id (int): Repull-internal alteration id (`reservation_alterations.id`). Example: 4471.
            channel (str): Source channel. Currently always `airbnb`. Example: airbnb.
            reservation_id (int): Repull reservation id the alteration targets. Pass to `GET /v1/reservations/{id}`.
                Example: 215906.
            customer_id (int): Workspace (customer) id. Example: 1.
            status (AlterationWebhookObjectStatus): Alteration lifecycle status. Example: pending.
            alteration_id (None | str | Unset): Provider-side alteration/resolution id. Example: RAX9K2M4C1.
            initiator (AlterationWebhookObjectInitiatorType1 | AlterationWebhookObjectInitiatorType2Type1 |
                AlterationWebhookObjectInitiatorType3Type1 | None | Unset): Who requested the alteration. Example: guest.
     """

    id: int
    channel: str
    reservation_id: int
    customer_id: int
    status: AlterationWebhookObjectStatus
    alteration_id: None | str | Unset = UNSET
    initiator: AlterationWebhookObjectInitiatorType1 | AlterationWebhookObjectInitiatorType2Type1 | AlterationWebhookObjectInitiatorType3Type1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel = self.channel

        reservation_id = self.reservation_id

        customer_id = self.customer_id

        status = self.status.value

        alteration_id: None | str | Unset
        if isinstance(self.alteration_id, Unset):
            alteration_id = UNSET
        else:
            alteration_id = self.alteration_id

        initiator: None | str | Unset
        if isinstance(self.initiator, Unset):
            initiator = UNSET
        elif isinstance(self.initiator, AlterationWebhookObjectInitiatorType1):
            initiator = self.initiator.value
        elif isinstance(self.initiator, AlterationWebhookObjectInitiatorType2Type1):
            initiator = self.initiator.value
        elif isinstance(self.initiator, AlterationWebhookObjectInitiatorType3Type1):
            initiator = self.initiator.value
        else:
            initiator = self.initiator


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "channel": channel,
            "reservationId": reservation_id,
            "customerId": customer_id,
            "status": status,
        })
        if alteration_id is not UNSET:
            field_dict["alterationId"] = alteration_id
        if initiator is not UNSET:
            field_dict["initiator"] = initiator

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        channel = d.pop("channel")

        reservation_id = d.pop("reservationId")

        customer_id = d.pop("customerId")

        status = AlterationWebhookObjectStatus(d.pop("status"))




        def _parse_alteration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alteration_id = _parse_alteration_id(d.pop("alterationId", UNSET))


        def _parse_initiator(data: object) -> AlterationWebhookObjectInitiatorType1 | AlterationWebhookObjectInitiatorType2Type1 | AlterationWebhookObjectInitiatorType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initiator_type_1 = AlterationWebhookObjectInitiatorType1(data)



                return initiator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initiator_type_2_type_1 = AlterationWebhookObjectInitiatorType2Type1(data)



                return initiator_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initiator_type_3_type_1 = AlterationWebhookObjectInitiatorType3Type1(data)



                return initiator_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlterationWebhookObjectInitiatorType1 | AlterationWebhookObjectInitiatorType2Type1 | AlterationWebhookObjectInitiatorType3Type1 | None | Unset, data)

        initiator = _parse_initiator(d.pop("initiator", UNSET))


        alteration_webhook_object = cls(
            id=id,
            channel=channel,
            reservation_id=reservation_id,
            customer_id=customer_id,
            status=status,
            alteration_id=alteration_id,
            initiator=initiator,
        )


        alteration_webhook_object.additional_properties = d
        return alteration_webhook_object

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
