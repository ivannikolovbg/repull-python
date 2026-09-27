from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SubmitCloudbedsCredentialsResponse200AccountInfo")



@_attrs_define
class SubmitCloudbedsCredentialsResponse200AccountInfo:
    """ 
        Attributes:
            external_account_id (str | Unset): The Cloudbeds property id these credentials belong to.
            account_name (None | str | Unset):
            property_ids (list[str] | Unset): Every property the credentials cover.
     """

    external_account_id: str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    property_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        external_account_id = self.external_account_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        property_ids: list[str] | Unset = UNSET
        if not isinstance(self.property_ids, Unset):
            property_ids = self.property_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if property_ids is not UNSET:
            field_dict["propertyIds"] = property_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_account_id = d.pop("externalAccountId", UNSET)

        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        property_ids = cast(list[str], d.pop("propertyIds", UNSET))


        submit_cloudbeds_credentials_response_200_account_info = cls(
            external_account_id=external_account_id,
            account_name=account_name,
            property_ids=property_ids,
        )


        submit_cloudbeds_credentials_response_200_account_info.additional_properties = d
        return submit_cloudbeds_credentials_response_200_account_info

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
