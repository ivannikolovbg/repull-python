from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitMewsCredentialsResponse200Webhooks")



@_attrs_define
class SubmitMewsCredentialsResponse200Webhooks:
    """ 
        Attributes:
            registered (int | Unset): Webhook subscriptions created at the PMS (Cloudbeds). Mews webhooks are enabled once
                per integration by Mews, so this is 0 there.
            error (str | Unset): Why subscribing failed, if it did. The connection still syncs by polling.
     """

    registered: int | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        registered = self.registered

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if registered is not UNSET:
            field_dict["registered"] = registered
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registered = d.pop("registered", UNSET)

        error = d.pop("error", UNSET)

        submit_mews_credentials_response_200_webhooks = cls(
            registered=registered,
            error=error,
        )


        submit_mews_credentials_response_200_webhooks.additional_properties = d
        return submit_mews_credentials_response_200_webhooks

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
