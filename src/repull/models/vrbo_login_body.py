from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_login_body_access_type import VrboLoginBodyAccessType
from ..models.vrbo_login_body_action import VrboLoginBodyAction
from ..types import UNSET, Unset






T = TypeVar("T", bound="VrboLoginBody")



@_attrs_define
class VrboLoginBody:
    """ 
        Attributes:
            session_id (str):
            action (VrboLoginBodyAction):
            email (str | Unset):
            password (str | Unset):
            account_id (int | Unset):
            code (str | Unset):
            access_type (VrboLoginBodyAccessType | Unset):
     """

    session_id: str
    action: VrboLoginBodyAction
    email: str | Unset = UNSET
    password: str | Unset = UNSET
    account_id: int | Unset = UNSET
    code: str | Unset = UNSET
    access_type: VrboLoginBodyAccessType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        action = self.action.value

        email = self.email

        password = self.password

        account_id = self.account_id

        code = self.code

        access_type: str | Unset = UNSET
        if not isinstance(self.access_type, Unset):
            access_type = self.access_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessionId": session_id,
            "action": action,
        })
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if code is not UNSET:
            field_dict["code"] = code
        if access_type is not UNSET:
            field_dict["accessType"] = access_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId")

        action = VrboLoginBodyAction(d.pop("action"))




        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        account_id = d.pop("accountId", UNSET)

        code = d.pop("code", UNSET)

        _access_type = d.pop("accessType", UNSET)
        access_type: VrboLoginBodyAccessType | Unset
        if isinstance(_access_type,  Unset):
            access_type = UNSET
        else:
            access_type = VrboLoginBodyAccessType(_access_type)




        vrbo_login_body = cls(
            session_id=session_id,
            action=action,
            email=email,
            password=password,
            account_id=account_id,
            code=code,
            access_type=access_type,
        )


        vrbo_login_body.additional_properties = d
        return vrbo_login_body

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
