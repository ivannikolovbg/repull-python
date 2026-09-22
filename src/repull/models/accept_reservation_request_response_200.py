from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.accept_reservation_request_response_200_action import AcceptReservationRequestResponse200Action
from ..models.accept_reservation_request_response_200_channel import AcceptReservationRequestResponse200Channel
from ..models.accept_reservation_request_response_200_decline_reason_type_1 import AcceptReservationRequestResponse200DeclineReasonType1
from ..models.accept_reservation_request_response_200_decline_reason_type_2_type_1 import AcceptReservationRequestResponse200DeclineReasonType2Type1
from ..models.accept_reservation_request_response_200_decline_reason_type_3_type_1 import AcceptReservationRequestResponse200DeclineReasonType3Type1
from ..models.accept_reservation_request_response_200_status import AcceptReservationRequestResponse200Status
from typing import cast






T = TypeVar("T", bound="AcceptReservationRequestResponse200")



@_attrs_define
class AcceptReservationRequestResponse200:
    """ 
        Attributes:
            reservation_id (str):  Example: 236354.
            confirmation_code (str):  Example: HM9J2MFR3W.
            channel (AcceptReservationRequestResponse200Channel):
            action (AcceptReservationRequestResponse200Action):
            status (AcceptReservationRequestResponse200Status): What Airbnb was asked to do and did not refuse. The
                reservation itself moves when Airbnb’s own notification lands, usually within seconds — that is when
                `reservation.request.updated` fires (`requestStatus` `accepted` or `declined`), plus `reservation.created` for
                an accepted request.
            decline_reason (AcceptReservationRequestResponse200DeclineReasonType1 |
                AcceptReservationRequestResponse200DeclineReasonType2Type1 |
                AcceptReservationRequestResponse200DeclineReasonType3Type1 | None):
     """

    reservation_id: str
    confirmation_code: str
    channel: AcceptReservationRequestResponse200Channel
    action: AcceptReservationRequestResponse200Action
    status: AcceptReservationRequestResponse200Status
    decline_reason: AcceptReservationRequestResponse200DeclineReasonType1 | AcceptReservationRequestResponse200DeclineReasonType2Type1 | AcceptReservationRequestResponse200DeclineReasonType3Type1 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id = self.reservation_id

        confirmation_code = self.confirmation_code

        channel = self.channel.value

        action = self.action.value

        status = self.status.value

        decline_reason: None | str
        if isinstance(self.decline_reason, AcceptReservationRequestResponse200DeclineReasonType1):
            decline_reason = self.decline_reason.value
        elif isinstance(self.decline_reason, AcceptReservationRequestResponse200DeclineReasonType2Type1):
            decline_reason = self.decline_reason.value
        elif isinstance(self.decline_reason, AcceptReservationRequestResponse200DeclineReasonType3Type1):
            decline_reason = self.decline_reason.value
        else:
            decline_reason = self.decline_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservationId": reservation_id,
            "confirmationCode": confirmation_code,
            "channel": channel,
            "action": action,
            "status": status,
            "declineReason": decline_reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservation_id = d.pop("reservationId")

        confirmation_code = d.pop("confirmationCode")

        channel = AcceptReservationRequestResponse200Channel(d.pop("channel"))




        action = AcceptReservationRequestResponse200Action(d.pop("action"))




        status = AcceptReservationRequestResponse200Status(d.pop("status"))




        def _parse_decline_reason(data: object) -> AcceptReservationRequestResponse200DeclineReasonType1 | AcceptReservationRequestResponse200DeclineReasonType2Type1 | AcceptReservationRequestResponse200DeclineReasonType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decline_reason_type_1 = AcceptReservationRequestResponse200DeclineReasonType1(data)



                return decline_reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decline_reason_type_2_type_1 = AcceptReservationRequestResponse200DeclineReasonType2Type1(data)



                return decline_reason_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decline_reason_type_3_type_1 = AcceptReservationRequestResponse200DeclineReasonType3Type1(data)



                return decline_reason_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AcceptReservationRequestResponse200DeclineReasonType1 | AcceptReservationRequestResponse200DeclineReasonType2Type1 | AcceptReservationRequestResponse200DeclineReasonType3Type1 | None, data)

        decline_reason = _parse_decline_reason(d.pop("declineReason"))


        accept_reservation_request_response_200 = cls(
            reservation_id=reservation_id,
            confirmation_code=confirmation_code,
            channel=channel,
            action=action,
            status=status,
            decline_reason=decline_reason,
        )


        accept_reservation_request_response_200.additional_properties = d
        return accept_reservation_request_response_200

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
