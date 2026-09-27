from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_mews_credentials_body_credentials_environment import SubmitMewsCredentialsBodyCredentialsEnvironment
from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitMewsCredentialsBodyCredentials")



@_attrs_define
class SubmitMewsCredentialsBodyCredentials:
    """ The property's Mews Connector API access token.

        Attributes:
            access_token (str): The property's Connector API access token.
            environment (SubmitMewsCredentialsBodyCredentialsEnvironment | Unset): `demo` targets Mews's public demo
                environment. Default: SubmitMewsCredentialsBodyCredentialsEnvironment.PRODUCTION.
     """

    access_token: str
    environment: SubmitMewsCredentialsBodyCredentialsEnvironment | Unset = SubmitMewsCredentialsBodyCredentialsEnvironment.PRODUCTION
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accessToken": access_token,
        })
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("accessToken")

        _environment = d.pop("environment", UNSET)
        environment: SubmitMewsCredentialsBodyCredentialsEnvironment | Unset
        if isinstance(_environment,  Unset):
            environment = UNSET
        else:
            environment = SubmitMewsCredentialsBodyCredentialsEnvironment(_environment)




        submit_mews_credentials_body_credentials = cls(
            access_token=access_token,
            environment=environment,
        )


        submit_mews_credentials_body_credentials.additional_properties = d
        return submit_mews_credentials_body_credentials

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
