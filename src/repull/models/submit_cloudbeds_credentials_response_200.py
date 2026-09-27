from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_cloudbeds_credentials_response_200_account_info import SubmitCloudbedsCredentialsResponse200AccountInfo
  from ..models.submit_cloudbeds_credentials_response_200_webhooks import SubmitCloudbedsCredentialsResponse200Webhooks





T = TypeVar("T", bound="SubmitCloudbedsCredentialsResponse200")



@_attrs_define
class SubmitCloudbedsCredentialsResponse200:
    """ 
        Attributes:
            provider (str | Unset):  Example: cloudbeds.
            connected (bool | Unset):
            pms_connection_id (str | Unset): Id of the stored connection.
            created (bool | Unset): False when an existing connection was updated.
            session_id (None | str | Unset):
            account_info (SubmitCloudbedsCredentialsResponse200AccountInfo | Unset):
            webhooks (SubmitCloudbedsCredentialsResponse200Webhooks | Unset):
     """

    provider: str | Unset = UNSET
    connected: bool | Unset = UNSET
    pms_connection_id: str | Unset = UNSET
    created: bool | Unset = UNSET
    session_id: None | str | Unset = UNSET
    account_info: SubmitCloudbedsCredentialsResponse200AccountInfo | Unset = UNSET
    webhooks: SubmitCloudbedsCredentialsResponse200Webhooks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_cloudbeds_credentials_response_200_account_info import SubmitCloudbedsCredentialsResponse200AccountInfo
        from ..models.submit_cloudbeds_credentials_response_200_webhooks import SubmitCloudbedsCredentialsResponse200Webhooks
        provider = self.provider

        connected = self.connected

        pms_connection_id = self.pms_connection_id

        created = self.created

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        account_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_info, Unset):
            account_info = self.account_info.to_dict()

        webhooks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = self.webhooks.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if connected is not UNSET:
            field_dict["connected"] = connected
        if pms_connection_id is not UNSET:
            field_dict["pmsConnectionId"] = pms_connection_id
        if created is not UNSET:
            field_dict["created"] = created
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if account_info is not UNSET:
            field_dict["accountInfo"] = account_info
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_cloudbeds_credentials_response_200_account_info import SubmitCloudbedsCredentialsResponse200AccountInfo
        from ..models.submit_cloudbeds_credentials_response_200_webhooks import SubmitCloudbedsCredentialsResponse200Webhooks
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        connected = d.pop("connected", UNSET)

        pms_connection_id = d.pop("pmsConnectionId", UNSET)

        created = d.pop("created", UNSET)

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("sessionId", UNSET))


        _account_info = d.pop("accountInfo", UNSET)
        account_info: SubmitCloudbedsCredentialsResponse200AccountInfo | Unset
        if isinstance(_account_info,  Unset):
            account_info = UNSET
        else:
            account_info = SubmitCloudbedsCredentialsResponse200AccountInfo.from_dict(_account_info)




        _webhooks = d.pop("webhooks", UNSET)
        webhooks: SubmitCloudbedsCredentialsResponse200Webhooks | Unset
        if isinstance(_webhooks,  Unset):
            webhooks = UNSET
        else:
            webhooks = SubmitCloudbedsCredentialsResponse200Webhooks.from_dict(_webhooks)




        submit_cloudbeds_credentials_response_200 = cls(
            provider=provider,
            connected=connected,
            pms_connection_id=pms_connection_id,
            created=created,
            session_id=session_id,
            account_info=account_info,
            webhooks=webhooks,
        )


        submit_cloudbeds_credentials_response_200.additional_properties = d
        return submit_cloudbeds_credentials_response_200

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
