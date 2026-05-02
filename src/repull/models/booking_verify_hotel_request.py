from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BookingVerifyHotelRequest")



@_attrs_define
class BookingVerifyHotelRequest:
    """ Body for `POST /v1/connect/booking/verify`. Manual-paste fallback that closes a Booking.com Connect session after
    the customer completes Stage 1 designation in the Extranet.

        Attributes:
            session_id (str): The Connect session ID returned by `createConnectSession`. Acts as the capability token — no
                API key required. Example: cs_8gQrT2v9k3M4nLp7wJxYzAbCdEfGhIjKlMnOp.
            hotel_id (str): Booking.com hotel ID the customer pasted. 6+ digits. Example: 12345678.
     """

    session_id: str
    hotel_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        hotel_id = self.hotel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessionId": session_id,
            "hotelId": hotel_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId")

        hotel_id = d.pop("hotelId")

        booking_verify_hotel_request = cls(
            session_id=session_id,
            hotel_id=hotel_id,
        )


        booking_verify_hotel_request.additional_properties = d
        return booking_verify_hotel_request

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
