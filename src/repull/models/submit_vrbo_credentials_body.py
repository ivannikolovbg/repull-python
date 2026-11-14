from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitVrboCredentialsBody")



@_attrs_define
class SubmitVrboCredentialsBody:
    """ 
        Attributes:
            advertiser_external_id (str): The host's Vrbo advertiser id. Repull mints the Basic-Auth pair for it, which the
                host pastes into Vrbo Partner Central.
            session_id (str | Unset): Connect session id from `POST /v1/connect/vrbo`.
            endpoint_url (str | Unset): Optional. Vrbo Partner Central sets this itself.
            rotate (bool | Unset): Replace the advertiser's existing password and return the new one. The old password stops
                working.
     """

    advertiser_external_id: str
    session_id: str | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    rotate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        advertiser_external_id = self.advertiser_external_id

        session_id = self.session_id

        endpoint_url = self.endpoint_url

        rotate = self.rotate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "advertiserExternalId": advertiser_external_id,
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if endpoint_url is not UNSET:
            field_dict["endpointUrl"] = endpoint_url
        if rotate is not UNSET:
            field_dict["rotate"] = rotate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advertiser_external_id = d.pop("advertiserExternalId")

        session_id = d.pop("sessionId", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        rotate = d.pop("rotate", UNSET)

        submit_vrbo_credentials_body = cls(
            advertiser_external_id=advertiser_external_id,
            session_id=session_id,
            endpoint_url=endpoint_url,
            rotate=rotate,
        )


        submit_vrbo_credentials_body.additional_properties = d
        return submit_vrbo_credentials_body

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
