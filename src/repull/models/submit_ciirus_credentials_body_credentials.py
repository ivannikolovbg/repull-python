from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitCiirusCredentialsBodyCredentials")



@_attrs_define
class SubmitCiirusCredentialsBodyCredentials:
    """ The CiiRUS API username and password.

        Attributes:
            api_username (str): CiiRUS API username, from the CiiRUS API Explorer or CiiRUS support.
            api_password (str): CiiRUS API password.
            management_company_user_id (int | Unset): The CiiRUS supplier (management company) id, the MCUserID. Only needed
                when the credentials see several suppliers. Example: 42330.
     """

    api_username: str
    api_password: str
    management_company_user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_username = self.api_username

        api_password = self.api_password

        management_company_user_id = self.management_company_user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiUsername": api_username,
            "apiPassword": api_password,
        })
        if management_company_user_id is not UNSET:
            field_dict["managementCompanyUserId"] = management_company_user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_username = d.pop("apiUsername")

        api_password = d.pop("apiPassword")

        management_company_user_id = d.pop("managementCompanyUserId", UNSET)

        submit_ciirus_credentials_body_credentials = cls(
            api_username=api_username,
            api_password=api_password,
            management_company_user_id=management_company_user_id,
        )


        submit_ciirus_credentials_body_credentials.additional_properties = d
        return submit_ciirus_credentials_body_credentials

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
