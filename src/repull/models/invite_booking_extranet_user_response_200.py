from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="InviteBookingExtranetUserResponse200")



@_attrs_define
class InviteBookingExtranetUserResponse200:
    """ 
        Attributes:
            account_id (int | Unset):
            invite_email (str | Unset):
            invite_name (str | Unset):
            two_factor_number (str | Unset):
     """

    account_id: int | Unset = UNSET
    invite_email: str | Unset = UNSET
    invite_name: str | Unset = UNSET
    two_factor_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        invite_email = self.invite_email

        invite_name = self.invite_name

        two_factor_number = self.two_factor_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if invite_email is not UNSET:
            field_dict["inviteEmail"] = invite_email
        if invite_name is not UNSET:
            field_dict["inviteName"] = invite_name
        if two_factor_number is not UNSET:
            field_dict["twoFactorNumber"] = two_factor_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        invite_email = d.pop("inviteEmail", UNSET)

        invite_name = d.pop("inviteName", UNSET)

        two_factor_number = d.pop("twoFactorNumber", UNSET)

        invite_booking_extranet_user_response_200 = cls(
            account_id=account_id,
            invite_email=invite_email,
            invite_name=invite_name,
            two_factor_number=two_factor_number,
        )


        invite_booking_extranet_user_response_200.additional_properties = d
        return invite_booking_extranet_user_response_200

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
