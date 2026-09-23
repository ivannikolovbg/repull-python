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
  from ..models.inquiry_updated_payload_previous_attributes import InquiryUpdatedPayloadPreviousAttributes
  from ..models.inquiry_webhook_object import InquiryWebhookObject





T = TypeVar("T", bound="InquiryUpdatedPayload")



@_attrs_define
class InquiryUpdatedPayload:
    """ Payload for `inquiry.updated`. The inquiry's status, dates, guest count or the reservation it became changed.
    `previousAttributes` holds only what moved, with prior values. Fires whether the host acted through the API, a
    connected app or the Airbnb app. An inquiry whose dates simply pass is `expired` in `GET /v1/inquiries` but fires no
    event unless the channel reports it.

        Attributes:
            object_ (InquiryWebhookObject): An inquiry — a guest asking about dates before booking — exactly as `GET
                /v1/inquiries` returns it. Delivered as `data.object` on `inquiry.*` events.
            previous_attributes (InquiryUpdatedPayloadPreviousAttributes): Keys of `object` that moved (`status`, `checkIn`,
                `checkOut`, `guests`, `reservationId`), mapped to their prior values. Example: {'status': 'open'}.
            occurred_at (datetime.datetime | Unset):
            revision (datetime.datetime | None | Unset):
     """

    object_: InquiryWebhookObject
    previous_attributes: InquiryUpdatedPayloadPreviousAttributes
    occurred_at: datetime.datetime | Unset = UNSET
    revision: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inquiry_updated_payload_previous_attributes import InquiryUpdatedPayloadPreviousAttributes
        from ..models.inquiry_webhook_object import InquiryWebhookObject
        object_ = self.object_.to_dict()

        previous_attributes = self.previous_attributes.to_dict()

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        revision: None | str | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        elif isinstance(self.revision, datetime.datetime):
            revision = self.revision.isoformat()
        else:
            revision = self.revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
            "previousAttributes": previous_attributes,
        })
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inquiry_updated_payload_previous_attributes import InquiryUpdatedPayloadPreviousAttributes
        from ..models.inquiry_webhook_object import InquiryWebhookObject
        d = dict(src_dict)
        object_ = InquiryWebhookObject.from_dict(d.pop("object"))




        previous_attributes = InquiryUpdatedPayloadPreviousAttributes.from_dict(d.pop("previousAttributes"))




        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at,  Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)




        def _parse_revision(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revision_type_0 = isoparse(data)



                return revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))


        inquiry_updated_payload = cls(
            object_=object_,
            previous_attributes=previous_attributes,
            occurred_at=occurred_at,
            revision=revision,
        )


        inquiry_updated_payload.additional_properties = d
        return inquiry_updated_payload

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
