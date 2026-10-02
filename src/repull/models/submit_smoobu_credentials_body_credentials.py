from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SubmitSmoobuCredentialsBodyCredentials")



@_attrs_define
class SubmitSmoobuCredentialsBodyCredentials:
    """ HMAC API key + secret from Smoobu → Settings → Advanced → API Keys.

        Attributes:
            api_key (str): Smoobu API key.
            api_secret (str): Smoobu API secret (shown once when generated).
     """

    api_key: str
    api_secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        api_secret = self.api_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "apiSecret": api_secret,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        api_secret = d.pop("apiSecret")

        submit_smoobu_credentials_body_credentials = cls(
            api_key=api_key,
            api_secret=api_secret,
        )


        submit_smoobu_credentials_body_credentials.additional_properties = d
        return submit_smoobu_credentials_body_credentials

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
