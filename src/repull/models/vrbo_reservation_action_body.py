from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_reservation_action_body_action import VrboReservationActionBodyAction
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="VrboReservationActionBody")



@_attrs_define
class VrboReservationActionBody:
    """ 
        Attributes:
            action (VrboReservationActionBodyAction):
            reason (str | Unset): `cancel`: Vrbo's cancel reason; `decline`: Vrbo's decline reason; `refund`: why.
            message (str | Unset): Sent to the guest. `cancel` 25–250 characters (required); `charge` ≤ 50 (required);
                `accept`/`decline` ≤ 250.
            refund_level (str | Unset): `cancel`: the refund Vrbo offers for the reason (default `FULL`). Example: FULL.
            block_dates (bool | Unset): `decline`: also block the requested dates.
            fee_type (str | Unset): `charge`: Vrbo's fee type. Example: PARKING.
            amount (float | Unset): `charge`/`refund`: the amount, in the booking's currency. Example: 25.
            due_date (datetime.date | Unset): `charge`: when the guest must pay (default today).
            preview (bool | Unset): Vrbo's dry run only (cancel, charge, refund): nothing is changed.
     """

    action: VrboReservationActionBodyAction
    reason: str | Unset = UNSET
    message: str | Unset = UNSET
    refund_level: str | Unset = UNSET
    block_dates: bool | Unset = UNSET
    fee_type: str | Unset = UNSET
    amount: float | Unset = UNSET
    due_date: datetime.date | Unset = UNSET
    preview: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        reason = self.reason

        message = self.message

        refund_level = self.refund_level

        block_dates = self.block_dates

        fee_type = self.fee_type

        amount = self.amount

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        preview = self.preview


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if refund_level is not UNSET:
            field_dict["refund_level"] = refund_level
        if block_dates is not UNSET:
            field_dict["block_dates"] = block_dates
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = VrboReservationActionBodyAction(d.pop("action"))




        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        refund_level = d.pop("refund_level", UNSET)

        block_dates = d.pop("block_dates", UNSET)

        fee_type = d.pop("fee_type", UNSET)

        amount = d.pop("amount", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: datetime.date | Unset
        if isinstance(_due_date,  Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()




        preview = d.pop("preview", UNSET)

        vrbo_reservation_action_body = cls(
            action=action,
            reason=reason,
            message=message,
            refund_level=refund_level,
            block_dates=block_dates,
            fee_type=fee_type,
            amount=amount,
            due_date=due_date,
            preview=preview,
        )

        return vrbo_reservation_action_body

