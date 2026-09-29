from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetBookingExtranetLoginStatusResponse200")



@_attrs_define
class GetBookingExtranetLoginStatusResponse200:
    """ 
        Attributes:
            account_id (int | Unset):
            status (str | Unset):
            error_message (str | Unset):
            friendly_error (str | Unset):
            completed (bool | Unset):
            awaiting_mapping (bool | Unset):
     """

    account_id: int | Unset = UNSET
    status: str | Unset = UNSET
    error_message: str | Unset = UNSET
    friendly_error: str | Unset = UNSET
    completed: bool | Unset = UNSET
    awaiting_mapping: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        status = self.status

        error_message = self.error_message

        friendly_error = self.friendly_error

        completed = self.completed

        awaiting_mapping = self.awaiting_mapping


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if friendly_error is not UNSET:
            field_dict["friendlyError"] = friendly_error
        if completed is not UNSET:
            field_dict["completed"] = completed
        if awaiting_mapping is not UNSET:
            field_dict["awaitingMapping"] = awaiting_mapping

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        status = d.pop("status", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        friendly_error = d.pop("friendlyError", UNSET)

        completed = d.pop("completed", UNSET)

        awaiting_mapping = d.pop("awaitingMapping", UNSET)

        get_booking_extranet_login_status_response_200 = cls(
            account_id=account_id,
            status=status,
            error_message=error_message,
            friendly_error=friendly_error,
            completed=completed,
            awaiting_mapping=awaiting_mapping,
        )


        get_booking_extranet_login_status_response_200.additional_properties = d
        return get_booking_extranet_login_status_response_200

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
