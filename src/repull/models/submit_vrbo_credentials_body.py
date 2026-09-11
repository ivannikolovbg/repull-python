from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_vrbo_credentials_body_credentials import SubmitVrboCredentialsBodyCredentials





T = TypeVar("T", bound="SubmitVrboCredentialsBody")



@_attrs_define
class SubmitVrboCredentialsBody:
    """ 
        Attributes:
            credentials (SubmitVrboCredentialsBodyCredentials): Activation handshake — Repull mints the Basic-Auth pair the
                host pastes into Vrbo Partner Central.
            session_id (str | Unset): Connect session id from `POST /v1/connect/vrbo`.
     """

    credentials: SubmitVrboCredentialsBodyCredentials
    session_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_vrbo_credentials_body_credentials import SubmitVrboCredentialsBodyCredentials
        credentials = self.credentials.to_dict()

        session_id = self.session_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credentials": credentials,
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_vrbo_credentials_body_credentials import SubmitVrboCredentialsBodyCredentials
        d = dict(src_dict)
        credentials = SubmitVrboCredentialsBodyCredentials.from_dict(d.pop("credentials"))




        session_id = d.pop("sessionId", UNSET)

        submit_vrbo_credentials_body = cls(
            credentials=credentials,
            session_id=session_id,
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
