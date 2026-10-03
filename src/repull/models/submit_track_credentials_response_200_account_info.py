from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_track_credentials_response_200_account_info_auth_mode import SubmitTrackCredentialsResponse200AccountInfoAuthMode
from ..models.submit_track_credentials_response_200_account_info_key_type import SubmitTrackCredentialsResponse200AccountInfoKeyType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SubmitTrackCredentialsResponse200AccountInfo")



@_attrs_define
class SubmitTrackCredentialsResponse200AccountInfo:
    """ 
        Attributes:
            domain (str | Unset): The Track host the connection calls. Example: acme.trackhs.com.
            key_type (SubmitTrackCredentialsResponse200AccountInfoKeyType | Unset):
            auth_mode (SubmitTrackCredentialsResponse200AccountInfoAuthMode | Unset):
            account_name (None | str | Unset):
     """

    domain: str | Unset = UNSET
    key_type: SubmitTrackCredentialsResponse200AccountInfoKeyType | Unset = UNSET
    auth_mode: SubmitTrackCredentialsResponse200AccountInfoAuthMode | Unset = UNSET
    account_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        key_type: str | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value


        auth_mode: str | Unset = UNSET
        if not isinstance(self.auth_mode, Unset):
            auth_mode = self.auth_mode.value


        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domain is not UNSET:
            field_dict["domain"] = domain
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if account_name is not UNSET:
            field_dict["accountName"] = account_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        _key_type = d.pop("keyType", UNSET)
        key_type: SubmitTrackCredentialsResponse200AccountInfoKeyType | Unset
        if isinstance(_key_type,  Unset):
            key_type = UNSET
        else:
            key_type = SubmitTrackCredentialsResponse200AccountInfoKeyType(_key_type)




        _auth_mode = d.pop("authMode", UNSET)
        auth_mode: SubmitTrackCredentialsResponse200AccountInfoAuthMode | Unset
        if isinstance(_auth_mode,  Unset):
            auth_mode = UNSET
        else:
            auth_mode = SubmitTrackCredentialsResponse200AccountInfoAuthMode(_auth_mode)




        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        submit_track_credentials_response_200_account_info = cls(
            domain=domain,
            key_type=key_type,
            auth_mode=auth_mode,
            account_name=account_name,
        )


        submit_track_credentials_response_200_account_info.additional_properties = d
        return submit_track_credentials_response_200_account_info

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
