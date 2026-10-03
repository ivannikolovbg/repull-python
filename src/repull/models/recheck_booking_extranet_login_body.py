from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RecheckBookingExtranetLoginBody")



@_attrs_define
class RecheckBookingExtranetLoginBody:
    """ 
        Attributes:
            session_id (str): The Connect session ID (capability token).
            account_id (int): The Booking.com direct-login connection id returned when the sign-in started.
     """

    session_id: str
    account_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        account_id = self.account_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessionId": session_id,
            "accountId": account_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId")

        account_id = d.pop("accountId")

        recheck_booking_extranet_login_body = cls(
            session_id=session_id,
            account_id=account_id,
        )


        recheck_booking_extranet_login_body.additional_properties = d
        return recheck_booking_extranet_login_body

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
