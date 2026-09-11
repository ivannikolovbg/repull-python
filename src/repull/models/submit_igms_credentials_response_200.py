from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_igms_credentials_response_200_account_info import SubmitIgmsCredentialsResponse200AccountInfo





T = TypeVar("T", bound="SubmitIgmsCredentialsResponse200")



@_attrs_define
class SubmitIgmsCredentialsResponse200:
    """ 
        Attributes:
            ok (bool | Unset):
            account_info (SubmitIgmsCredentialsResponse200AccountInfo | Unset):
     """

    ok: bool | Unset = UNSET
    account_info: SubmitIgmsCredentialsResponse200AccountInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_igms_credentials_response_200_account_info import SubmitIgmsCredentialsResponse200AccountInfo
        ok = self.ok

        account_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_info, Unset):
            account_info = self.account_info.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ok is not UNSET:
            field_dict["ok"] = ok
        if account_info is not UNSET:
            field_dict["accountInfo"] = account_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_igms_credentials_response_200_account_info import SubmitIgmsCredentialsResponse200AccountInfo
        d = dict(src_dict)
        ok = d.pop("ok", UNSET)

        _account_info = d.pop("accountInfo", UNSET)
        account_info: SubmitIgmsCredentialsResponse200AccountInfo | Unset
        if isinstance(_account_info,  Unset):
            account_info = UNSET
        else:
            account_info = SubmitIgmsCredentialsResponse200AccountInfo.from_dict(_account_info)




        submit_igms_credentials_response_200 = cls(
            ok=ok,
            account_info=account_info,
        )


        submit_igms_credentials_response_200.additional_properties = d
        return submit_igms_credentials_response_200

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
