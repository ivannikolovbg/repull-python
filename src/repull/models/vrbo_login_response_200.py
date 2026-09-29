from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_login_response_200_status import VrboLoginResponse200Status
from ..types import UNSET, Unset






T = TypeVar("T", bound="VrboLoginResponse200")



@_attrs_define
class VrboLoginResponse200:
    """ 
        Attributes:
            account_id (int | Unset):
            status (VrboLoginResponse200Status | Unset):
            reason (str | Unset):
            error (str | Unset):
            destination (str | Unset):
            notification_email (str | Unset):
            awaiting_mapping (bool | Unset):
     """

    account_id: int | Unset = UNSET
    status: VrboLoginResponse200Status | Unset = UNSET
    reason: str | Unset = UNSET
    error: str | Unset = UNSET
    destination: str | Unset = UNSET
    notification_email: str | Unset = UNSET
    awaiting_mapping: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        reason = self.reason

        error = self.error

        destination = self.destination

        notification_email = self.notification_email

        awaiting_mapping = self.awaiting_mapping


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if error is not UNSET:
            field_dict["error"] = error
        if destination is not UNSET:
            field_dict["destination"] = destination
        if notification_email is not UNSET:
            field_dict["notificationEmail"] = notification_email
        if awaiting_mapping is not UNSET:
            field_dict["awaitingMapping"] = awaiting_mapping

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        _status = d.pop("status", UNSET)
        status: VrboLoginResponse200Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = VrboLoginResponse200Status(_status)




        reason = d.pop("reason", UNSET)

        error = d.pop("error", UNSET)

        destination = d.pop("destination", UNSET)

        notification_email = d.pop("notificationEmail", UNSET)

        awaiting_mapping = d.pop("awaitingMapping", UNSET)

        vrbo_login_response_200 = cls(
            account_id=account_id,
            status=status,
            reason=reason,
            error=error,
            destination=destination,
            notification_email=notification_email,
            awaiting_mapping=awaiting_mapping,
        )


        vrbo_login_response_200.additional_properties = d
        return vrbo_login_response_200

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
