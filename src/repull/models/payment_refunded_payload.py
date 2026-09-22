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
  from ..models.payment_webhook_object import PaymentWebhookObject





T = TypeVar("T", bound="PaymentRefundedPayload")



@_attrs_define
class PaymentRefundedPayload:
    """ Payload for `payment.refunded`. Money went back. Covers both a refund-typed movement and any adjustment with a
    negative amount — the sign on `object.amount` is preserved so the direction never has to be inferred.

        Attributes:
            object_ (PaymentWebhookObject): A money movement: a guest charge, a host payout, a refund, a tourist-tax pass-
                through, a resolution payout, or an adjustment that claws money back.
            refunded_at (datetime.datetime | None | Unset):
            reason (None | str | Unset):  Example: Resolution centre adjustment.
            revision (datetime.datetime | None | Unset):
     """

    object_: PaymentWebhookObject
    refunded_at: datetime.datetime | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    revision: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_webhook_object import PaymentWebhookObject
        object_ = self.object_.to_dict()

        refunded_at: None | str | Unset
        if isinstance(self.refunded_at, Unset):
            refunded_at = UNSET
        elif isinstance(self.refunded_at, datetime.datetime):
            refunded_at = self.refunded_at.isoformat()
        else:
            refunded_at = self.refunded_at

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

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
        })
        if refunded_at is not UNSET:
            field_dict["refundedAt"] = refunded_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_webhook_object import PaymentWebhookObject
        d = dict(src_dict)
        object_ = PaymentWebhookObject.from_dict(d.pop("object"))




        def _parse_refunded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refunded_at_type_0 = isoparse(data)



                return refunded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        refunded_at = _parse_refunded_at(d.pop("refundedAt", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


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


        payment_refunded_payload = cls(
            object_=object_,
            refunded_at=refunded_at,
            reason=reason,
            revision=revision,
        )


        payment_refunded_payload.additional_properties = d
        return payment_refunded_payload

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
