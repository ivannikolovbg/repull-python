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
  from ..models.reservation_cancelled_payload_refund_type_0 import ReservationCancelledPayloadRefundType0





T = TypeVar("T", bound="ReservationCancelledPayload")



@_attrs_define
class ReservationCancelledPayload:
    """ Payload for `reservation.cancelled`. A reservation was cancelled by the guest, host, or platform.

        Attributes:
            id (int | Unset):  Example: 215906.
            confirmation_code (str | Unset):  Example: HMA1234567.
            cancelled_at (datetime.datetime | Unset):  Example: 2026-05-01T14:00:00.000Z.
            cancelled_by (str | Unset): Who initiated the cancellation (guest, host, platform). Example: guest.
            reason (None | str | Unset):  Example: guest_requested.
            refund (None | ReservationCancelledPayloadRefundType0 | Unset):
     """

    id: int | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    cancelled_at: datetime.datetime | Unset = UNSET
    cancelled_by: str | Unset = UNSET
    reason: None | str | Unset = UNSET
    refund: None | ReservationCancelledPayloadRefundType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_cancelled_payload_refund_type_0 import ReservationCancelledPayloadRefundType0
        id = self.id

        confirmation_code = self.confirmation_code

        cancelled_at: str | Unset = UNSET
        if not isinstance(self.cancelled_at, Unset):
            cancelled_at = self.cancelled_at.isoformat()

        cancelled_by = self.cancelled_by

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        refund: dict[str, Any] | None | Unset
        if isinstance(self.refund, Unset):
            refund = UNSET
        elif isinstance(self.refund, ReservationCancelledPayloadRefundType0):
            refund = self.refund.to_dict()
        else:
            refund = self.refund


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if cancelled_at is not UNSET:
            field_dict["cancelledAt"] = cancelled_at
        if cancelled_by is not UNSET:
            field_dict["cancelledBy"] = cancelled_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if refund is not UNSET:
            field_dict["refund"] = refund

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_cancelled_payload_refund_type_0 import ReservationCancelledPayloadRefundType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        confirmation_code = d.pop("confirmationCode", UNSET)

        _cancelled_at = d.pop("cancelledAt", UNSET)
        cancelled_at: datetime.datetime | Unset
        if isinstance(_cancelled_at,  Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = isoparse(_cancelled_at)




        cancelled_by = d.pop("cancelledBy", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_refund(data: object) -> None | ReservationCancelledPayloadRefundType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                refund_type_0 = ReservationCancelledPayloadRefundType0.from_dict(data)



                return refund_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReservationCancelledPayloadRefundType0 | Unset, data)

        refund = _parse_refund(d.pop("refund", UNSET))


        reservation_cancelled_payload = cls(
            id=id,
            confirmation_code=confirmation_code,
            cancelled_at=cancelled_at,
            cancelled_by=cancelled_by,
            reason=reason,
            refund=refund,
        )


        reservation_cancelled_payload.additional_properties = d
        return reservation_cancelled_payload

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
