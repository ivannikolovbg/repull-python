from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SubmitCiirusCredentialsResponse200AccountInfo")



@_attrs_define
class SubmitCiirusCredentialsResponse200AccountInfo:
    """ 
        Attributes:
            supplier_id (str | Unset): The CiiRUS supplier (management company) id the connection reads. Example: 42330.
            account_name (None | str | Unset): The supplier's company name.
     """

    supplier_id: str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        supplier_id = self.supplier_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if supplier_id is not UNSET:
            field_dict["supplierId"] = supplier_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supplier_id = d.pop("supplierId", UNSET)

        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        submit_ciirus_credentials_response_200_account_info = cls(
            supplier_id=supplier_id,
            account_name=account_name,
        )


        submit_ciirus_credentials_response_200_account_info.additional_properties = d
        return submit_ciirus_credentials_response_200_account_info

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
