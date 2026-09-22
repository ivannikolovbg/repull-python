from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_reservation_action_body_action import AirbnbReservationActionBodyAction
from ..models.airbnb_reservation_action_body_reason import AirbnbReservationActionBodyReason
from ..types import UNSET, Unset






T = TypeVar("T", bound="AirbnbReservationActionBody")



@_attrs_define
class AirbnbReservationActionBody:
    """ 
        Attributes:
            action (AirbnbReservationActionBodyAction):
            reason (AirbnbReservationActionBodyReason | Unset): Required for `decline` and `cancel`; not accepted for
                `accept`. `decline` takes `dates_not_available`, `not_comfortable`, `listing_not_ready`,
                `different_dates_needed`, `spam` or `other`. `cancel` takes `calendar_conflict`, `maintenance_issue`,
                `unable_to_host` or `other`.
            message (str | Unset): Required for `decline` only: sent to the guest by Airbnb.
     """

    action: AirbnbReservationActionBodyAction
    reason: AirbnbReservationActionBodyReason | Unset = UNSET
    message: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value


        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = AirbnbReservationActionBodyAction(d.pop("action"))




        _reason = d.pop("reason", UNSET)
        reason: AirbnbReservationActionBodyReason | Unset
        if isinstance(_reason,  Unset):
            reason = UNSET
        else:
            reason = AirbnbReservationActionBodyReason(_reason)




        message = d.pop("message", UNSET)

        airbnb_reservation_action_body = cls(
            action=action,
            reason=reason,
            message=message,
        )

        return airbnb_reservation_action_body

