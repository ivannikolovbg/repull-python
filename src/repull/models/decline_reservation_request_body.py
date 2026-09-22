from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.decline_reservation_request_body_reason import DeclineReservationRequestBodyReason






T = TypeVar("T", bound="DeclineReservationRequestBody")



@_attrs_define
class DeclineReservationRequestBody:
    """ 
        Attributes:
            reason (DeclineReservationRequestBodyReason): Airbnb’s decline reason, verbatim. `dates_not_available` — the
                dates are taken; `not_comfortable` — you are not comfortable with the booking; `listing_not_ready` — the listing
                cannot be booked right now; `different_dates_needed` — you want different dates; `spam` — the request is spam;
                `other` — anything else (explain in `message`).
            message (str): Sent to the guest by Airbnb with the decline. Example: Sorry, those dates are no longer
                available..
     """

    reason: DeclineReservationRequestBodyReason
    message: str





    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "reason": reason,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = DeclineReservationRequestBodyReason(d.pop("reason"))




        message = d.pop("message")

        decline_reservation_request_body = cls(
            reason=reason,
            message=message,
        )

        return decline_reservation_request_body

