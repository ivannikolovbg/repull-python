from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.hospitable_webhook import HospitableWebhook
  from ..models.submit_hospitable_credentials_response_200_account_info import SubmitHospitableCredentialsResponse200AccountInfo





T = TypeVar("T", bound="SubmitHospitableCredentialsResponse200")



@_attrs_define
class SubmitHospitableCredentialsResponse200:
    """ 
        Attributes:
            ok (bool | Unset):
            account_info (SubmitHospitableCredentialsResponse200AccountInfo | Unset):
            webhook (HospitableWebhook | None | Unset): The webhook URL to show the host: in Hospitable, Apps → Webhooks → +
                Add new, paste it, tick Reservations, Messages, Properties and Reviews. Optional — without it the connection is
                polled every minute. `null` if it could not be set up.
     """

    ok: bool | Unset = UNSET
    account_info: SubmitHospitableCredentialsResponse200AccountInfo | Unset = UNSET
    webhook: HospitableWebhook | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.hospitable_webhook import HospitableWebhook
        from ..models.submit_hospitable_credentials_response_200_account_info import SubmitHospitableCredentialsResponse200AccountInfo
        ok = self.ok

        account_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_info, Unset):
            account_info = self.account_info.to_dict()

        webhook: dict[str, Any] | None | Unset
        if isinstance(self.webhook, Unset):
            webhook = UNSET
        elif isinstance(self.webhook, HospitableWebhook):
            webhook = self.webhook.to_dict()
        else:
            webhook = self.webhook


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ok is not UNSET:
            field_dict["ok"] = ok
        if account_info is not UNSET:
            field_dict["accountInfo"] = account_info
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hospitable_webhook import HospitableWebhook
        from ..models.submit_hospitable_credentials_response_200_account_info import SubmitHospitableCredentialsResponse200AccountInfo
        d = dict(src_dict)
        ok = d.pop("ok", UNSET)

        _account_info = d.pop("accountInfo", UNSET)
        account_info: SubmitHospitableCredentialsResponse200AccountInfo | Unset
        if isinstance(_account_info,  Unset):
            account_info = UNSET
        else:
            account_info = SubmitHospitableCredentialsResponse200AccountInfo.from_dict(_account_info)




        def _parse_webhook(data: object) -> HospitableWebhook | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                webhook_type_1 = HospitableWebhook.from_dict(data)



                return webhook_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HospitableWebhook | None | Unset, data)

        webhook = _parse_webhook(d.pop("webhook", UNSET))


        submit_hospitable_credentials_response_200 = cls(
            ok=ok,
            account_info=account_info,
            webhook=webhook,
        )


        submit_hospitable_credentials_response_200.additional_properties = d
        return submit_hospitable_credentials_response_200

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
