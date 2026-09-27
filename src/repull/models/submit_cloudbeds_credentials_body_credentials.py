from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SubmitCloudbedsCredentialsBodyCredentials")



@_attrs_define
class SubmitCloudbedsCredentialsBodyCredentials:
    """ A Cloudbeds API key (starts with `cbat_`).

        Attributes:
            api_key (str): Cloudbeds API key.
            property_ids (list[str] | Unset): Organization keys only: limit the connection to these properties. Omit to use
                every property the key can see.
     """

    api_key: str
    property_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        property_ids: list[str] | Unset = UNSET
        if not isinstance(self.property_ids, Unset):
            property_ids = self.property_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
        })
        if property_ids is not UNSET:
            field_dict["propertyIds"] = property_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        property_ids = cast(list[str], d.pop("propertyIds", UNSET))


        submit_cloudbeds_credentials_body_credentials = cls(
            api_key=api_key,
            property_ids=property_ids,
        )


        submit_cloudbeds_credentials_body_credentials.additional_properties = d
        return submit_cloudbeds_credentials_body_credentials

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
