from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_cloudbeds_credentials_body_credentials import SubmitCloudbedsCredentialsBodyCredentials
  from ..models.submit_cloudbeds_credentials_body_write_policy import SubmitCloudbedsCredentialsBodyWritePolicy





T = TypeVar("T", bound="SubmitCloudbedsCredentialsBody")



@_attrs_define
class SubmitCloudbedsCredentialsBody:
    """ 
        Attributes:
            credentials (SubmitCloudbedsCredentialsBodyCredentials): A Cloudbeds API key (starts with `cbat_`).
            session_id (str | Unset): Connect session id from `POST /v1/connect/cloudbeds`. Omit when calling with your API
                key.
            write_policy (SubmitCloudbedsCredentialsBodyWritePolicy | Unset): Optional: what the app may change in the PMS,
                set before the first sync. Same shape as `PATCH /v1/connect/{provider}/write-policy`; switches you leave out
                keep the provider default (calendar off for hotel PMSs, bookings on). Example: {'calendar': {'rates': True}}.
     """

    credentials: SubmitCloudbedsCredentialsBodyCredentials
    session_id: str | Unset = UNSET
    write_policy: SubmitCloudbedsCredentialsBodyWritePolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_cloudbeds_credentials_body_credentials import SubmitCloudbedsCredentialsBodyCredentials
        from ..models.submit_cloudbeds_credentials_body_write_policy import SubmitCloudbedsCredentialsBodyWritePolicy
        credentials = self.credentials.to_dict()

        session_id = self.session_id

        write_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.write_policy, Unset):
            write_policy = self.write_policy.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credentials": credentials,
        })
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if write_policy is not UNSET:
            field_dict["writePolicy"] = write_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_cloudbeds_credentials_body_credentials import SubmitCloudbedsCredentialsBodyCredentials
        from ..models.submit_cloudbeds_credentials_body_write_policy import SubmitCloudbedsCredentialsBodyWritePolicy
        d = dict(src_dict)
        credentials = SubmitCloudbedsCredentialsBodyCredentials.from_dict(d.pop("credentials"))




        session_id = d.pop("sessionId", UNSET)

        _write_policy = d.pop("writePolicy", UNSET)
        write_policy: SubmitCloudbedsCredentialsBodyWritePolicy | Unset
        if isinstance(_write_policy,  Unset):
            write_policy = UNSET
        else:
            write_policy = SubmitCloudbedsCredentialsBodyWritePolicy.from_dict(_write_policy)




        submit_cloudbeds_credentials_body = cls(
            credentials=credentials,
            session_id=session_id,
            write_policy=write_policy,
        )


        submit_cloudbeds_credentials_body.additional_properties = d
        return submit_cloudbeds_credentials_body

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
